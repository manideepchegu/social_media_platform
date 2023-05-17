from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/<int:post_id>/likes", methods=["PUT"], endpoint="update_like")
@handle_exceptions
def update_like(post_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for creating likes")
    try:
        if cur and conn:
            cur.execute("UPDATE post_data SET like_count = like_count + 1 WHERE post_id = %s", (post_id,))
            conn.commit()
            return {"message": "Post liked successfully"}, 200
        else:
            return {"message": "Failed to like post"}, 500
    except Exception as e:
        return {"message": "Error occurred while liking the post", "error": str(e)}, 500

