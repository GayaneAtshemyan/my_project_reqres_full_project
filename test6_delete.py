import requests
import pytest
import allure

class TestDeleteUser():
    @allure.feature("delete functionality")
    @allure.story("Delete User")
    @pytest.mark.regression
    def test_delete_user(self):
        user_id = 2
        url = f"https://reqres.in/api/users/{user_id}"

        with allure.step(f"Send DELETE request to delete user {user_id}"):
            response = requests.delete(url)

        with allure.step("Check the status code"):
            assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

