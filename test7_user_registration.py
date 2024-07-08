import requests
import pytest
import allure

@allure.feature("Registration")
class TestUserRegistration():
    @allure.feature("Registration")
    @allure.story("Register User-Successful")
    @pytest.mark.regression
    def test_register_user(self):
        url = "https://reqres.in/api/register"
        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        # Send POST request to register user
        with allure.step("Send POST request to register user"):
            response = requests.post(url, json=payload)

        # Check status code
        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # Check response body
        with allure.step("Check the response body"):
            response_json = response.json()
            assert "id" in response_json, "Response JSON does not contain 'id'"
            assert "token" in response_json, "Response JSON does not contain 'token'"
            assert isinstance(response_json["id"], int), "id should be an integer"
            assert isinstance(response_json["token"], str), "token should be a string"

    @allure.feature("Registration")
    @allure.story("Register User - Unsuccessful")
    @pytest.mark.regression
    def test_register_unsuccessful(self):
        url = "https://reqres.in/api/register"
        payload = {
            "email": "sydney@fife"
        }

        with allure.step("Send POST request to register user with missing password"):
            response = requests.post(url, json=payload)

        with allure.step("Verify the status code"):
            assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"

        with allure.step("Verify the error message"):
            response_json = response.json()
            assert "error" in response_json, "Response JSON does not contain 'error'"
            assert response_json["error"] == "Missing password", f"Expected 'Missing password' error message"
#
# import requests
# import pytest
# import allure
#
# # Base URL for the API
# base_url = "https://reqres.in/api"
#
#
# @allure.feature("API Tests")
# @allure.story("User Registration")
# class TestUserRegistration:
#
#     @allure.title("Successful Registration")
#     @pytest.mark.parametrize("email, password", [
#         ("eve.holt@reqres.in", "pistol"), ])
#     def test_successful_registration(self, email, password):
#         url = f"{base_url}/register"
#         payload = {
#             "email": email,
#             "password": password
#         }
#
#         with allure.step(f"Registering user with email '{email}'"):
#             response = requests.post(url, json=payload)
#
#         with allure.step("Verifying response"):
#             assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
#             response_json = response.json()
#             assert "id" in response_json, "Response JSON does not contain 'id'"
#             assert "token" in response_json, "Response JSON does not contain 'token'"
#             assert isinstance(response_json["id"], int), "id should be an integer"
#             assert isinstance(response_json["token"], str), "token should be a string"
#
#     @allure.title("Registration with Existing Email")
#     def test_registration_with_existing_email(self):
#         url = f"{base_url}/register"
#         payload = {
#             "email": "eve.holt@reqres.in",
#             "password": "pistol"
#         }
#
#         with allure.step("Registering user with existing email 'eve.holt@reqres.in'"):
#             response = requests.post(url, json=payload)
#
#         with allure.step("Verifying response"):
#             assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
#             response_json = response.json()
#             assert "error" in response_json, "Response JSON does not contain 'error'"
#             assert "email" in response_json["error"], "Response JSON error does not indicate email issue"
#
#     @allure.title("Registration with Missing Fields")
#     @pytest.mark.parametrize("payload", [
#         {"password": "pistol"},
#         {"email": "eve.holt@reqres.in"},
#         {}
#     ])
#     def test_registration_with_missing_fields(self, payload):
#         url = f"{base_url}/register"
#
#         with allure.step(f"Registering user with payload: {payload}"):
#             response = requests.post(url, json=payload)
#
#         with allure.step("Verifying response"):
#             assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
#             response_json = response.json()
#             assert "error" in response_json, "Response JSON does not contain 'error'"
#             assert "email" in response_json.get("error", {}) or "password" in response_json.get("error", {}), \
#                 "Response JSON error does not indicate missing email or password field"
#
#     @allure.title("Registration with Invalid Email Format")
#     @pytest.mark.parametrize("email", [
#         "eve.holt.reqres.in",
#         "eve.holt@reqres",
#         "eve.holt@reqres.",
#         "eve.holt@reqres@in"
#     ])
#     def test_registration_with_invalid_email_format(self, email):
#         url = f"{base_url}/register"
#         payload = {
#             "email": email,
#             "password": "pistol"
#         }
#
#         with allure.step(f"Registering user with invalid email '{email}'"):
#             response = requests.post(url, json=payload)
#
#         with allure.step("Verifying response"):
#             assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
#             response_json = response.json()
#             assert "error" in response_json, "Response JSON does not contain 'error'"
#             assert "email" in response_json.get("error", {}), "Response JSON error does not indicate email format issue"
