import requests
import allure
from jsonschema.validators import validate
from conftest import load_json_schema, api_request


project = 'catfact'


def test_breeds_list_smoke():
    request = api_request(project, '/breeds')

    with allure.step(f'Status code = {request.status_code}'):
        assert request.status_code == 200


def test_breeds_list_schema():
    schema = load_json_schema(project, 'breeds_list.json')

    request = api_request(project, '/breeds')

    with allure.step('Validate Schema'):
        validate(request.json(), schema=schema)


def test_breeds_list_limit():
    request = api_request(project, '/breeds', params={'limit': 3})

    with allure.step('Validate per_page parameter'):
        assert int(request.json()['per_page']) == 3
