from shutil import ExecError
from flask import Flask, make_response, request, jsonify
import build
from flask_mail import Message, Mail
import json
import gitfunctions
import build
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin
from test import Test
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/jacob/test.db"
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app, session_options={"expire_on_commit":False})


from utils import *
from model import Build

db.create_all()


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

tempDir = "./temp-git-dir/"
currentBranch = "master"
allowTests = True

@app.route("/github", methods=["POST"])
def webhook_message():
    """
    Endpoint for Github webhooks to send data for push events.
    Clones the edited branch, conducts syntax checking and saves
    the build result to a database.

    Returns:
        201 if the data was saved correctly, 400 if the input JSON parameters
        or X-Github-Event header is incorrect
    """
    if (
        "X-Github-Event" in request.headers
        and request.headers["X-Github-Event"] == "push"
    ):
        try:
            info = json.dumps(request.json)
            data = json.loads(info)
            newBuild = save_json_to_build(data)
            currentBranch = newBuild.branch
            gitRepo = gitfunctions.GitRepo(tempDir, currentBranch)
            syntaxCheck = build.SyntaxCheck(
                tempDir + "Assignment2/server.py"
            )
            update_build_with_syntax_check(newBuild, syntaxCheck.result)
            if allowTests:
                print(gitRepo.repoLocalPath + "Assignment2/tests")
                testing = Test(gitRepo.repoLocalPath + "Assignment2/tests")
                update_build_with_test_result(newBuild, testing.result)
                msg = create_email_message(data, syntaxCheck.result, testing.result)
                mail.send(msg)
                res = {"build_result": syntaxCheck.result, "test_result": testing.result, "error": ""}
                return make_response(jsonify(res), 201)
            else:
                msg = create_email_message(data, syntaxCheck.result, False)
                res = {"build_result": syntaxCheck.result, "error": ""}
                mail.send(msg)
                return make_response(jsonify(res), 201)
        except Exception as e:
            print(e)
            res = {"build_result": "", "error": "The JSON body is incorrect"}
            return make_response(jsonify(res), 400)
    elif (
        "X-Github-Event" in request.headers
        and request.headers["X-Github-Event"] == "ping"
    ):
        return make_response(jsonify({}), 200)
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
    app.run(debug=False, port=4567)
