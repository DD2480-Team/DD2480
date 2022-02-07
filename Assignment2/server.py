from __future__ import print_function
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return "HOME PAGE!"

#testing Jacobs PR
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
        return "sucess"


if __name__=='__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True,  port=4567)
