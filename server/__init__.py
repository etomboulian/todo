from flask import Flask

app = Flask(__name__)

from .routes.people import bp
app.register_blueprint(bp)

@app.route("/", methods=["GET"])
def home_page():
    return "<h2> Welcome to the home page </h2>"
