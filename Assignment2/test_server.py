import pytest
from server import webhook_message, app
import json


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

    Test result: Pass if status code being returned is 201
    """

    url = "/github"
    with open("test_success_body.json") as f:
        data = json.load(f)
    header = {"X-Github-Event": "push"}

    rv = client.post(url, json=data, headers=header)
    assert rv.status_code == 201
