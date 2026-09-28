from fastapi.testclient import TestClient

from dmud.main import create_app


def test_save_slots_returns_three_explicit_empty_slots() -> None:
    client = TestClient(create_app())

    response = client.get("/api/save-slots")

    assert response.status_code == 200
    assert response.json() == {
        "slots": [
            {"number": 1, "status": "empty"},
            {"number": 2, "status": "empty"},
            {"number": 3, "status": "empty"},
        ]
    }


def test_save_slots_read_does_not_change_subsequent_reads() -> None:
    client = TestClient(create_app())

    first = client.get("/api/save-slots")
    second = client.get("/api/save-slots")

    assert second.json() == first.json()
