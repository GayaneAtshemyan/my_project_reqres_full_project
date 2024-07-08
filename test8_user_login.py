import requests
import pytest
import allure

class TestLogin():
    @allure.feature("Login functionality")
    @allure.story("User Login-successfull")
    @pytest.mark.regression
    def test_login_successful(self):
        url = "https://reqres.in/api/login"
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        with allure.step("Send POST request to login"):
            response = requests.post(url, json=payload)

        with allure.step("Verify the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step("Verify the token in the response"):
            response_json = response.json()
            assert "token" in response_json, "Response JSON does not contain 'token'"
            assert isinstance(response_json["token"], str), "Token should be a string"


    @allure.feature("User functionality")
    @allure.story("User Login - Unsuccessful")
    @pytest.mark.regression
    def test_login_unsuccessful(self):
        url = "https://reqres.in/api/login"
        payload = {
            "email": "peter@klaven"
        }

        with allure.step("Send POST request to login with missing password"):
            response = requests.post(url, json=payload)

        with allure.step("Verify the status code"):
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        with allure.step("Verify the error message"):
            response_json = response.json()
            assert "error" in response_json, "Response JSON does not contain 'error'"
            assert response_json["error"] == "Missing password", "Expected 'Missing password' error message"



