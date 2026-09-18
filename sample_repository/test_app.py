"""Pytest suite for sample_repository FastAPI application.
Exposes seeded bug where empty phone numbers trigger an unhandled 500 error instead of a 400 response.
"""

import pytest
from fastapi.testclient import TestClient
from app import app, users_db


@pytest.fixture(autouse=True)
def clean_db():
    users_db.clear()


@pytest.fixture
def client():
    return TestClient(app, raise_server_exceptions=False)


def test_health_check(client):
    """Verifies that the health endpoint responds with 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_valid_user(client):
    """Verifies successful user creation with a valid 10-digit phone number."""
    payload = {
        "name": "Alex Johnson",
        "email": "alex@example.com",
        "phone": "4155552671",
    }
    response = client.post("/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Alex Johnson"
    assert data["phone"] == "+1 (415) 555-2671"


def test_create_user_with_empty_phone_should_return_400(client):
    """Target bug test: creating a user with an empty phone number should return 400 Bad Request.
    
    CURRENT BEHAVIOR (FAILING): Missing validation in create_user() causes format_phone_number()
    to raise an unhandled ValueError, resulting in an HTTP 500 Internal Server Error.
    """
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "",
    }
    response = client.post("/users", json=payload)

    # Expected behavior after patch: 400 Bad Request with validation message
    assert response.status_code == 400, f"Expected 400 Bad Request, but got {response.status_code}: {response.text}"
    assert "detail" in response.json()
