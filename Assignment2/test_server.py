import pytest
from server import webhook_message, app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_webhook_message(client):
    url = "/github" 
    body= {"repository": {
            "owner": {
                "name": "DD2480-Team",
                "email": "NULL"
                }
            }
        }
    header = {
        "X-Github-Event":'push'
        }
    
    rv = client.post(url, json=body, headers=header)
    result =  rv.data
    assert result.decode() == "success"