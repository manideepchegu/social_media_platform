from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/comments/<int:post_id>",methods=["PUT"],endpoint="comments")
@handle_exceptions
def comments(post_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for deleting post")
    data = request.get_json()
    comments = data['comments']
    cur.execute('SELECT * FROM post_data WHERE post_id = %s', (post_id,))
    row = cur.fetchone()
    if not row:
        return jsonify({'message': 'post is not available'}), 400

    # Update the book's availability
    cur.execute('UPDATE post_data SET comments=%s WHERE post_id = %s', (comments,post_id,))
    conn.commit()

    return jsonify({'message': comments}), 200
