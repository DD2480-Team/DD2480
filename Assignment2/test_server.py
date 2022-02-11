import pytest
from server import webhook_message, app
from gitfunctions import GitRepo
import json
import os

testBranch = "push_for_testing"

@pytest.fixture
def client():
    """
    creates a specific app context for the test e.g. configuring the app database with specific values
    in this case, the context is just app in its current configuration
    the client object provides an interface for sending virtual requests to the applicatiton
    """
    with app.test_client() as client:
        yield client


# def test_webhook_message(client):
#     """
#     a simple test of the function webhook_message in server.py
#     the test is triggered by running "pytest test_server.py", and
#     simulates a post request to the webserver with
#     parameters:
#         url, body, and header
#     defined below

#     Args:
#         client (defined above): an interface to a specfically configured app instance

#     Test result: Pass if status code being returned is 201
#     """

#     url = "/github"
#     with open("test_success_body.json") as f:
#         data = json.load(f)
#     header = {"X-Github-Event": "push"}

#     rv = client.post(url, json=data, headers=header)
#     assert rv.status_code == 201

def test_git_pull_not_empty():
    """
    Creates a git object, performs a git clone,
    or if you already have the repo, just a git pull
    and then asserts that it is not empty
    """
    repo = GitRepo(testBranch)
    assert(repo.checkRepoNotBare() ==  True)

def test_git_pull_removed_file():
    """
    Creates a git object, forces a git clone,
    then REMOVES the server file and
    checks git status to see git is running and responds correctly
    """
    repo = GitRepo(testBranch)
    repo.forceClone(testBranch) #don't allow a local version of repo
    os.remove(repo.repoLocalPath + "Assignment2/server.py")
    gitStatus = repo.gitStatus()

    repo.forceClone(testBranch) #reset local files just in case someone runs this case in another case
    
    assert(gitStatus.find("deleted:    Assignment2/server.py") !=  -1)