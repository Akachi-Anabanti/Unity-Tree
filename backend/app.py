from flask import Flask


app = Flask(__name__)
app.register_blueprint(__name__, "api", url_prefix= 'api/v1')

