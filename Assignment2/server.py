from __future__ import print_function
from flask import Flask, request
from git import Repo
import json
import gitfunctions
import build
import test
import pathlib

app = Flask(__name__)

defaultBranch = "master"

@app.route('/')
def home_page():
    return "HOME PAGE!"

@app.route('/github', methods=['POST'])
def webhook_message():
    if request.method == "POST":
        if request.headers['X-Github-Event']=='push':
            info=json.dumps(request.json)
            data = json.loads(info)
            respository = data["repository"]
            owner = respository["owner"]
            name = owner["name"]
            email = owner["email"]
            message = "user: {} \nemail: {}".format(name,email)
            print(message)
            #create a git repo object, from which you can change branches as you please
            gitRepo = gitfunctions.GitRepo(defaultBranch)

            syntaxCheck = build.SyntaxCheck(gitRepo.repoLocalPath + "Assignment2/server.py")
            if syntaxCheck.result == False:
                return "failure"

            # not sure if this is a valid method
            #print(str(pathlib.Path(__file__).parent.resolve()))
            #if gitRepo.repoLocalPath[2:] not in str(pathlib.Path(__file__).parent.resolve()):
            testing = test.Test(gitRepo.repoLocalPath + "Assignment2/test_server.py")
            if testing.result == False:
                return "failure"
            
            return "success"

if __name__=='__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True,  port=4567)
