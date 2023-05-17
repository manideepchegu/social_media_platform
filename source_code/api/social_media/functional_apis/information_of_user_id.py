from flask import Flask, jsonify
from social_media.source_code.api.settings  import logger, connection, handle_exceptions
from social_media.source_code.api import app


@app.route("/users/<int:user_id>", methods=["GET"], endpoint="user_information")
@handle_exceptions
def user_information(user_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT user_name,email_id FROM user_data WHERE user_id = %s',(user_id,))
    rows = cur.fetchone()
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    user_name, email_id = rows
    data = {
        'user_name': user_name,
        'email_id' : email_id
    }
    data_list.append(data)
    logger(__name__).warning("close the database connection")

    return jsonify({"message": user_id,  "details": data_list})
