from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/media/post/insert", methods=["POST"], endpoint="create_post")
@handle_exceptions
def create_post():
    # set database connection
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for creating post")
    # get the values from the user
    if "user_id" and "title" and "content" not in request.json:
        raise Exception("details are missing")
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    content = data.get('content')
    # insert query
    query = "INSERT INTO post_data(user_id, title, content) VALUES (%s,%s,%s)"
    values = user_id, title, content
    values = (user_id, title, content)
    # execute the query with required value
    cur.execute(query, values)
    # log the details into log file
    logger(__name__).info("user_id created")
    conn.commit()
    return jsonify({"message": "post_id is created"}), 500
