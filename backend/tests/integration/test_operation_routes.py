import json

from fastapi.testclient import TestClient

from dmud.main import create_app

REQUEST = {"requestId": "req_00000000-0000-4000-8000-000000000002"}


def test_creation_returns_recoverable_operation() -> None:
    with TestClient(create_app()) as client:
        response = client.post("/api/session-zero-drafts", json=REQUEST)
        assert response.status_code == 202
        operation = response.json()
        status = client.get(operation["statusUrl"])
        assert status.status_code == 200
        assert status.json()["subject"] == operation["subject"]
        duplicate = client.post("/api/session-zero-drafts", json=REQUEST)
        assert duplicate.json()["operationId"] == operation["operationId"]


def test_invalid_command_returns_secret_free_problem() -> None:
    with TestClient(create_app()) as client:
        response = client.post(
            "/api/session-zero-drafts", json={**REQUEST, "secret": "private-canary"}
        )
        assert response.status_code == 422
        assert response.headers["content-type"] == "application/problem+json"
        assert "private-canary" not in response.text


def test_event_replay_returns_only_newer_ids() -> None:
    with TestClient(create_app()) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        with client.stream(
            "GET", operation["eventsUrl"], headers={"Last-Event-ID": "1"}
        ) as response:
            lines = list(response.iter_lines())
        events = [json.loads(line[6:]) for line in lines if line.startswith("data: ")]
        assert events
        ids = [event["eventId"] for event in events]
        assert ids == sorted(set(ids))
        assert min(ids) > 1
        assert events[-1]["operation"]["status"] == "complete"


def test_unknown_operation_is_a_problem() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/api/operations/op_missing")
        assert response.status_code == 404
        assert response.headers["content-type"] == "application/problem+json"


def test_invalid_event_cursor_returns_polling_recovery_problem() -> None:
    with TestClient(create_app()) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        for cursor in ("-1", "999999", "invalid"):
            response = client.get(
                operation["eventsUrl"], headers={"Last-Event-ID": cursor}
            )
            assert response.status_code == 409
            assert response.json()["code"] == "invalid_event_cursor"


def test_changed_payload_for_accepted_request_is_a_typed_conflict() -> None:
    with TestClient(create_app()) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        conflict = client.post(
            "/api/session-zero-drafts", json={**REQUEST, "schemaVersion": 2}
        )
        assert conflict.status_code == 409
        assert conflict.json()["code"] == "request_conflict"
        assert conflict.json()["operation"]["operationId"] == operation["operationId"]


def test_canonical_defaults_recover_the_same_request() -> None:
    with TestClient(create_app()) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        duplicate = client.post(
            "/api/session-zero-drafts",
            json={
                **REQUEST,
                "schemaVersion": 1,
                "command": "create_session_zero_draft",
            },
        )
        assert duplicate.json()["operationId"] == operation["operationId"]


def test_problem_has_safe_correlation_context() -> None:
    with TestClient(create_app()) as client:
        response = client.get("/api/operations/private-canary")
        problem = response.json()
        assert problem["classification"] == "not_found"
        assert problem["correlationId"].startswith("cor_")
        assert problem["instance"] == "urn:dmud:request:" + problem["correlationId"]
        assert "private-canary" not in response.text
