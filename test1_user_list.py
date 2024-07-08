import requests
import allure
import pytest

@allure.feature('TEST USER/S GET - feature')
@allure.suite('TEST USER/S GET with correct structure- suite')

class TestUserList():


    @allure.title('Test Retrieve All Users')
    @allure.description('This test case verifies that the system retrieves all users')
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_list_users_get(self):
        with allure.step('Send GET request to the users endpoint'):
            url="https://reqres.in/api/users?page=2"
            response = requests.get(url)

        with allure.step('Verify the response status code is 200'):
            assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

        with allure.step("Check the response body"):
            response_json = response.json()
            assert "data" in response_json, "Response JSON does not contain 'data'"
            assert isinstance(response_json["data"], list), "'data' is not a list"

        with allure.step("Check the user list is not empty"):
            assert len(response_json["data"]) > 0, "No users found in the response"
        with allure.step("Check the user data id,email,firstname,lastname"):
            for user in response_json["data"]:
             assert "id" in user, "User object does not contain 'id'"
             assert "email" in user, "User object does not contain 'email'"
             assert "first_name" in user, "User object does not contain 'first_name'"
             assert "last_name" in user, "User object does not contain 'last_name'"


    @allure.story("Get Single User")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_get_single_user(self):
        url = "https://reqres.in/api/users/2"
        response = requests.get(url)

        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert "data" in response_json, "Response JSON does not contain 'data'"
            user = response_json["data"]
            assert "id" in user, "User object does not contain 'id'"
            assert user["id"] == 2, f"Expected user id 2, but got {user['id']}"
            assert "email" in user, "User object does not contain 'email'"
            assert "first_name" in user, "User object does not contain 'first_name'"
            assert "last_name" in user, "User object does not contain 'last_name'"
            assert "avatar" in user, "User object does not contain 'avatar'"

    @allure.feature("Non existing user")
    @allure.story("User Not Found")
    @pytest.mark.regression
    def test_user_not_found(self):
        url = "https://reqres.in/api/users/23"
        response = requests.get(url)

        with allure.step("Check the status code"):
            assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert response_json == {}, f"Expected empty JSON, but got {response_json}"




