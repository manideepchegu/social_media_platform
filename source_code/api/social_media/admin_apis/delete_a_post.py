from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/delete/<int:post_id>", methods=["DELETE"], endpoint="delete_post")
@handle_exceptions
def delete_post(post_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for deleting post")
    # Delete the post from the database
    cur = conn.cursor()
    cur.execute("DELETE * FROM post_data WHERE post_id = %s", (post_id,))
    conn.commit()

    # Close the database connection
    cur.close()
    conn.close()

    # Return a response indicating success
    return jsonify({"message": "Post deleted successfully"})

