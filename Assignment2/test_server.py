import pytest
from server import webhook_message, app


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

    Test result: Pass if webhook_message returns "success", else Fail
    """

    url = "/github"
    body = {"repository": {"owner": {"name": "DD2480-Team", "email": "NULL"}}}
    header = {"X-Github-Event": "push"}

    rv = client.post(url, json=body, headers=header)
    result = rv.data
    assert result.decode() == "success"
