from __future__ import print_function
import build
from flask import Flask, request
from flask_mail import Message, Mail
from git import Repo
import json
import gitfunctions
import build
import test
import pathlib
import os

app = Flask(__name__)
# configuration for the mail client
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
"""
uses os.environ.get to access secret variables stored in env/bin/activate
under the deactivate function in env/bin/activate include the lines:
export USER2480="the_email"
export PASS2480="the_password"
"""
app.config['MAIL_USERNAME'] = os.environ.get("USER2480")
app.config['MAIL_PASSWORD'] = os.environ.get("PASS2480")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

defaultBranch = "master"
allowTests = False

@app.route('/')
def home_page():
    return "HOME PAGE!"


@app.route('/email', methods=['POST'])
def email_notification():
    """
    basic email notification to whoever is the author listed in the push event. 
    The msg object can be used to format the contents of an email

    Returns:
        sends an email to whoever was the author listed in the push event
        returns "success"
    """
    if request.method == "POST":
        if request.headers['X-Github-Event'] == 'push':
            # parse the json
            info = json.dumps(request.json)
            data = json.loads(info)
            commits = data["commits"][0]
            author_info = commits["author"]
            name = author_info["name"]
            email = author_info["email"]
            # craft the email message"
            msg = Message("Hello {}, I am an email!".format(name), sender=os.environ.get("USER2480"),
                          recipients=[email])
            msg.body = "testing"
            msg.html = "<b>testing</>"
            mail.send(msg)
        return "success"


@app.route('/github', methods=['POST'])
def webhook_message():
    if request.method == "POST":
        if request.headers['X-Github-Event'] == 'push':
            info = json.dumps(request.json)
            data = json.loads(info)
            branch = data["ref"].split('/')[-1]
            respository = data["repository"]
            owner = respository["owner"]
            name = owner["name"]
            email = owner["email"]
            message = "user: {} \nemail: {}".format(name, email)
            print(message)





            #create a git repo object, from which you can change branches as you please
            gitRepo = gitfunctions.GitRepo(defaultBranch)

            syntaxCheck = build.SyntaxCheck(gitRepo.repoLocalPath + "Assignment2/server.py")
            if syntaxCheck.result == False:
                return "failure"
            
            if(allowTests):
                testing = test.Test(gitRepo.repoLocalPath + "Assignment2/test_server.py")
                if testing.result == False:
                    return "failure"
            else:
                return "success"
        else:
            return "Not a push event."







if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True,  port=4567)
