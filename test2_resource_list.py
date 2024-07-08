import requests
import pytest
import allure

@allure.feature('TEST RESOURCE/S GET - feature')
@allure.suite('TEST RESOURCE/S GET with correct structure- suite')
class TestResourceList():
    @allure.feature("API Tests")
    @allure.story("Get Unknown Resources List")
    @pytest.mark.regression
    def test_get_unknown_resources(self):
        url = "https://reqres.in/api/unknown"
        response = requests.get(url)

        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert "data" in response_json, "Response JSON does not contain 'data'"
            assert isinstance(response_json["data"], list), "'data' is not a list"

            for resource in response_json["data"]:
                assert "id" in resource, "Resource object does not contain 'id'"
                assert "name" in resource, "Resource object does not contain 'name'"
                assert "year" in resource, "Resource object does not contain 'year'"
                assert "color" in resource, "Resource object does not contain 'color'"
                assert "pantone_value" in resource, "Resource object does not contain 'pantone_value'"


    @allure.feature("TEST RESOURCE/S GET")
    @allure.story("Get Single Unknown Resource")
    @pytest.mark.regression
    def test_get_single_unknown_resource(self):
        url = "https://reqres.in/api/unknown/2"
        response = requests.get(url)

        with allure.step("Check the status code"):
            assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert "data" in response_json, "Response JSON does not contain 'data'"
            resource = response_json["data"]
            assert "id" in resource, "Resource object does not contain 'id'"
            assert resource["id"] == 2, f"Expected resource id 2, but got {resource['id']}"
            assert "name" in resource, "Resource object does not contain 'name'"
            assert "year" in resource, "Resource object does not contain 'year'"
            assert "color" in resource, "Resource object does not contain 'color'"
            assert "pantone_value" in resource, "Resource object does not contain 'pantone_value'"


    @allure.feature("TEST RESOURCE/S GET")
    @allure.story("Unknown Resource Not Found")
    @pytest.mark.regression
    def test_unknown_resource_not_found(self):
        url = "https://reqres.in/api/unknown/23"
        response = requests.get(url)

        with allure.step("Check the status code"):
            assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

        with allure.step("Check the response body"):
            response_json = response.json()
            assert response_json == {}, f"Expected empty JSON, but got {response_json}"

