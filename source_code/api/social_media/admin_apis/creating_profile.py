from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app



@app.route("/media/insert", methods=["POST"], endpoint="create_profile")
@handle_exceptions
def create_profile():
    # set database connection
    cur, conn = connection()
    logger(__name__).warning("starting the database connection for creating profile")
    if "user_name" and "email_id" and "password" not in request.json:
        raise Exception("details are missing")
    # get the values from the user
    data = request.get_json()
    user_name = data.get('user_name')
    email_id = data.get('email_id')
    password = data.get('password')
    # insert query
    query = "INSERT INTO user_data(user_name,email_id,password) VALUES (%s,%s,%s)"
    values = (user_name, email_id, password)
    # execute the query with required value
    cur.execute(query, values)
    # log the details into log file
    logger(__name__).info("user_id created")
    conn.commit()
    return jsonify({"message": "user_id is created"}), 500