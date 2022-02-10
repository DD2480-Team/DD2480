from shutil import ExecError
from flask import Flask, make_response, request, jsonify
import build
from flask_mail import Message, Mail
import json
import gitfunctions
import os
import build
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
db = SQLAlchemy(app)

from utils import *
from model import Build

db.create_all()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\sqlite\\test.db"
app.config["CORS_HEADERS"] = "Content-Type"


"""
uses os.environ.get to access secret variables stored in env/bin/activate
under the deactivate function in env/bin/activate include the lines:
export USER2480="the_email"
export PASS2480="the_password"
"""
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = os.environ.get("USER2480")
app.config["MAIL_PASSWORD"] = os.environ.get("PASS2480")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)

defaultBranch = "master"


@app.route("/")
def home_page():
    return "HOME PAGE!"


@app.route("/email", methods=["POST"])
def email_notification():
    """
    basic email notification to whoever is the author listed in the push event.
    The msg object can be used to format the contents of an email

    Returns:
        sends an email to whoever was the author listed in the push event
        returns "success"
    """
    if request.method == "POST":
        if request.headers["X-Github-Event"] == "push":
            # parse the json
            info = json.dumps(request.json)
            data = json.loads(info)
            commits = data["commits"][0]
            author_info = commits["author"]
            name = author_info["name"]
            email = author_info["email"]
            msg = Message(
                "Hello {}, I am an email!".format(name),
                sender="jacobmimms@gmail.com",
                recipients=[email],
            )
            msg.body = "testing"
            msg.html = "<b>testing</>"
            mail.send(msg)
        return "success"


@app.route("/github", methods=["POST"])
def webhook_message():
    if (
        "X-Github-Event" in request.headers
        and request.headers["X-Github-Event"] == "push"
    ):
        try:
            info = json.dumps(request.json)
            data = json.loads(info)
            newBuild = save_json_to_build(data)
            gitRepo = gitfunctions.GitRepo(newBuild.branch)
            syntaxCheck = build.SyntaxCheck(
                gitRepo.repoLocalPath + "Assignment2/server.py"
            )
            update_build_with_syntax_check(newBuild, syntaxCheck.result)
            data = {"build_result": syntaxCheck.result, "error": ""}
            return make_response(jsonify(data), 201)
        except:
            data = {"build_result": "", "error": "The JSON body is incorrect"}
            return make_response(jsonify(data), 400)
    else:
        data = {
            "build_result": "",
            "error": "Ensure the X-Github-Event header is set correctly",
        }
        return make_response(jsonify(data), 400)


@app.route("/history", methods=["GET"])
@cross_origin()
def get_history():
    try:
        builds = get_all_builds()
        data = {"builds": builds, "error": ""}
        return make_response(jsonify(data), 200)
    except:
        data = {"builds": [], "error": "Internal server error"}
        return make_response(jsonify(data), 500)


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True, port=4567)
