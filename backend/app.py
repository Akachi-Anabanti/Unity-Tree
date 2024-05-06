#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from api import api_v1_bp

app = Flask(__name__)
app.register_blueprint(api_v1_bp, url_prefix="/api/v1")


@app.route("/sanity")
def sanity_check():
    return jsonify({"message": "Hello World!"}), 200


if __name__ == "__main__":
    app.run(host="localhost", port="5000")
