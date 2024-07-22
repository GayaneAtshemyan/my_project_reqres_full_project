import pytest
import requests


@pytest.fixture(scope='session')
def auth_token():
    url = "https://reqres.in/api/register"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    response_json = response.json()
    assert "token" in response_json, "Response JSON does not contain 'token'"

    return response_json['token']