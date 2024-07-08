import requests
import pytest
import allure


@allure.feature("Update User and test full update")
class TestUpdateUserPut():

    @allure.feature("Update User")
    @allure.story("Update User Put")
    @pytest.mark.regression
    def test_update_user(self):
        user_id = 2
        url = f"https://reqres.in/api/users/{user_id}"
        payload = {
            "name": "morpheus",
            "job": "zion resident"
        }

        with allure.step(f"Send PUT request to update user {user_id}"):
            response = requests.put(url, json=payload)

        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert response_json["name"] == payload[
                "name"], f"Expected name to be {payload['name']}, but got {response_json['name']}"
            assert response_json["job"] == payload[
                "job"], f"Expected job to be {payload['job']}, but got {response_json['job']}"
            assert "updatedAt" in response_json, "Response JSON does not contain 'updatedAt'"

