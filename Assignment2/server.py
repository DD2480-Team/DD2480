from flask import Flask, request
import json
import gitfunctions
import build
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\sqlite\\test.db"
db = SQLAlchemy(app)

from model import Build

db.create_all()

defaultBranch = "push_for_testing"


@app.route("/")
def home_page():
    return "HOME PAGE!"


@app.route("/github", methods=["POST"])
def webhook_message():
    if request.method == "POST":
        if request.headers["X-Github-Event"] == "push":
            info = json.dumps(request.json)
            data = json.loads(info)
            respository = data["repository"]
            owner = respository["owner"]
            name = owner["name"]
            email = owner["email"]
            message = "user: {} \nemail: {}".format(name, email)
            print(message)
            # create a git repo object, from which you can change branches as you please
            gitRepo = gitfunctions.GitRepo(defaultBranch)
            syntaxCheck = build.SyntaxCheck(
                gitRepo.repoLocalPath + "Assignment2/server.py"
            )
            if syntaxCheck.result == True:
                return "success"
            else:
                return "failure"


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True, port=4567)
