import requests
import pytest
import allure


class TestPartialUpdateUserPatch():
    @allure.feature("API Tests")
    @allure.story("Update User")
    @pytest.mark.regression
    def test_patch_user(self, auth_token):
        user_id = 2
        url = f"https://reqres.in/api/users/{user_id}"
        payload = {
            "job": "zion resident"
        }

        # Send PATCH request to partially update user
        with allure.step(f"Send PATCH request to update user {user_id}"):
            response = requests.patch(url, json=payload)

        # Check status code
        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Check response body
        with allure.step("Check the response body"):
            response_json = response.json()
            assert response_json["job"] == payload[
                "job"], f"Expected job to be {payload['job']}, but got {response_json['job']}"
            assert "updatedAt" in response_json, "Response JSON does not contain 'updatedAt'"

