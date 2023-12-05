from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to the ICU data service!"


def test_get_icu_info():
    # Replace 'Sample_MMSA' with a valid MMSA value for testing
    response = client.get("/icu_info/Manhattan,%20KS")
    assert response.status_code == 200
    # Additional assertions based on the expected response can be added here


def test_get_hospitals_info():
    response = client.get("/hospitals_info")
    assert response.status_code == 200
    # Additional assertions based on the expected response can be added here
