import pytest
import requests

def test_response():
    response = requests.get('http://localhost:8000/')
    assert response
