import pytest
from fastapi.testclient import TestClient
from rustpytemplate.app import *

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_run_sum_endpoint():
    response = client.get("/run/sum/1/2")
    assert response.status_code == 200
    assert response.json() == {"message": "show_sum(1,2) = 3"}


def test_run_diff_endpoint():
    response = client.get("/run/diff/2/1")
    assert response.status_code == 200
    assert response.json() == {"message": "show_diff(2,1) = 1"}


if __name__ == "__main__":
    pytest.main()
