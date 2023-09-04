import allure
from jsonschema.validators import validate
from conftest import load_json_schema, api_request


project = 'reqres'


def test_users_smoke():
    request = api_request(project, '/users')

    with allure.step('Validate Status code'):
        assert request.status_code == 200


def test_users_schema():
    schema = load_json_schema(project, 'users_list.json')

    request = api_request(project, '/users')
    with allure.step('Validate Schema'):
        validate(request.json(), schema=schema)


def test_users_per_page():
    request = api_request(project, '/users', params={'per_page': 3})

    with allure.step('Validate per_page param'):
        assert request.json()['per_page'] == 3



