
from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route('/<int:user_id>/', methods=['GET'])
def get_posts(user_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for fetching all posts of user_id")
    if cur and conn:
        try:
            cur.execute("SELECT post_id,user_id,content,title FROM post_data WHERE user_id = %s", (user_id,))
            rows = cur.fetchall()
            if not rows:
                return jsonify({"message": f"No rows found "})
            data_list = []
            for row in rows:
                post_id, user_id, content, title = row
                data = {
                    "post_id": post_id,
                    "user_id": user_id,
                    "content": content,
                    "title": title
                }
                data_list.append(data)
        except Exception as e:
            print(e)
            return {"message": "Failed to get posts"}, 500
        finally:
            cur.close()
            conn.close()
        return jsonify(data_list), 200
    else:
        return {"message": "Failed to get posts"}, 500
