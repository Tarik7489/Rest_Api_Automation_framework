import pytest
from utils.api_helper import APIHelper

@pytest.fixture(scope="session")
# def api():
#     return APIHelper("https://jsonplaceholder.typicode.com")

def baseUrl():
    return APIHelper("https://api.escuelajs.co")