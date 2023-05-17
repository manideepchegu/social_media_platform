from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/likes_and_comments/<int:post_id>", methods=["GET"], endpoint="post_information")
@handle_exceptions
def user_information(post_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT comments,like_count FROM post_data WHERE post_id = %s',(post_id,))
    rows = cur.fetchone()
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    comments,like_count = rows
    data = {
        'comments': comments,
        'like_count': like_count
    }
    data_list.append(data)
    logger(__name__).warning("close the database connection")

    return jsonify({"message": post_id,  "details": data_list})
