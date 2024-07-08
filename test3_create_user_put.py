import requests
import pytest
import allure
from datetime import datetime

class TestUserCreation():
    @allure.feature("Create User-feature")
    @allure.story("Create User")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_create_user(self):
        url = "https://reqres.in/api/users"
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

        with allure.step("Send POST request to create user"):
            response = requests.post(url, json=payload)

        with allure.step("Check the status code"):
            assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert response_json["name"] == payload[
                "name"], f"Expected name to be {payload['name']}, but got {response_json['name']}"
            assert response_json["job"] == payload[
                "job"], f"Expected job to be {payload['job']}, but got {response_json['job']}"
            assert "id" in response_json, "Response JSON does not contain 'id'"
            assert "createdAt" in response_json, "Response JSON does not contain 'createdAt'"


