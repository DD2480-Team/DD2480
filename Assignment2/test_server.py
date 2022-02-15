import pytest
from server import webhook_message, app, currentBranch, tempDir
from gitfunctions import GitRepo
import json
import os

testBranch = "master"
testDir = "./test-git-dir/"

@pytest.fixture
def client():
    """
    creates a specific app context for the test e.g. configuring the app database with specific values
    in this case, the context is just app in its current configuration
    the client object provides an interface for sending virtual requests to the applicatiton
    """
    with app.test_client() as client:
        yield client


def test_webhook_message(client):
    """
    a simple test of the function webhook_message in server.py
    the test is triggered by running "pytest test_server.py", and
    simulates a post request to the webserver with
    parameters:
        url, body, and header
    defined below

    Args:
        client (defined above): an interface to a specfically configured app instance

    Test result: Pass if status code being returned is 404, as the endpoint doesn't exists
    """

    url = "/non_existent_endpoint"
    with open("test_success_body.json") as f:
        data = json.load(f)
    header = {"X-Github-Event": "push"}

    rv = client.post(url, json=data, headers=header)
    assert rv.status_code == 404

def test_syntax_check(client):
    """
    Test the syntax checking function of the cloned repo triggered by webhook.
    A repo cloned from master according to test_success_body.json will appear
    under temp-git-dir/Assignment2 and being syntax checked by the server.py in the
    cloned repo triggered by webhook. 

    Args:
        client (defined above): an interface to a specfically configured app instance

    Test result: Pass if syntax checking is done correctly. 
    """
    os.chdir("./temp-git-dir/Assignment2")
    url = "/github"
    with open("test_success_body.json") as f:
        data = json.load(f)
    header = {"X-Github-Event": "push"}
    rv = client.post(url, json=data, headers=header)
    
    os.chdir("../..")
    assert rv.status_code == 201
    
def test_git_pull_not_empty():
    """
    Creates a git object, performs a git clone,
    or if you already have the repo, just a git pull
    and then asserts that it is not empty
    """
    repo = GitRepo(testDir, testBranch)
    repo_is_not_bare = repo.checkRepoNotBare()
    assert(repo_is_not_bare)

def test_git_pull_removed_file():
    """
    Creates a git object, forces a git clone,
    then REMOVES the server file and
    checks git status to see git is running and responds correctly
    """
    repo = GitRepo(testDir, testBranch)
    repo.forceClone(testDir, testBranch) #don't allow a local version of repo
    os.remove(repo.repoLocalPath + "Assignment2/server.py")
    gitStatus = repo.gitStatus()
    repo.forceClone(testDir, testBranch) #reset local files just in case someone runs this case in another case
    assert(gitStatus.find("deleted:    Assignment2/server.py") !=  -1)

