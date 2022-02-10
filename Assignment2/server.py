from __future__ import print_function
from flask import Flask, request
from git import Repo
import json
import gitfunctions
app = Flask(__name__)

defaultBranch = "master"
import build

@app.route('/')
def home_page():
    return "HOME PAGE!"

@app.route('/github', methods=['POST'])
def webhook_message():
    if request.method == "POST":
        if request.headers['X-Github-Event']=='push':
            info=json.dumps(request.json)
            data = json.loads(info)
            branch = data["ref"].split('/')[-1]
            respository = data["repository"]
            owner = respository["owner"]
            name = owner["name"]
            email = owner["email"]
            message = "user: {} \nemail: {}".format(name,email)
            print(message)
            #create a git repo object, from which you can change branches as you please
            gitRepo = gitfunctions.GitRepo(branch)
            syntaxCheck = build.SyntaxCheck(gitRepo.repoLocalPath + "Assignment2/server.py")
            if syntaxCheck.result == True:
                return "success"
            else:
                return "failure"

if __name__=='__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True,  port=4567)
