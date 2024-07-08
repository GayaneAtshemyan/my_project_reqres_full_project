import requests
import pytest
import allure


@allure.feature("Delayed Users")
@allure.story("Delayed Response - Get Users")
@pytest.mark.regression
def test_delayed_response_get_users():
    url = "https://reqres.in/api/users"
    params = {
        "delay": 3
    }

    with allure.step("Send GET request to fetch users with delay"):
        response = requests.get(url, params=params)

    with allure.step("Verify the status code"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Verify the response structure"):
        response_json = response.json()
        assert "page" in response_json
        assert "per_page" in response_json
        assert "total" in response_json
        assert "total_pages" in response_json
        assert "data" in response_json
        assert len(response_json["data"]) == 6  # Assuming there are 6 users per page
        assert "support" in response_json
        assert "url" in response_json["support"]
        assert "text" in response_json["support"]

