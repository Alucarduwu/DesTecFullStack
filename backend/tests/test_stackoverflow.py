from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_answered_summary_endpoint():
    response = client.get("/api/stackoverflow/answered-summary")

    assert response.status_code == 200

    data = response.json()

    assert "answered" in data
    assert "unanswered" in data
    assert "total" in data

    assert isinstance(data["answered"], int)
    assert isinstance(data["unanswered"], int)
    assert isinstance(data["total"], int)


def test_highest_reputation_endpoint():
    response = client.get("/api/stackoverflow/highest-reputation")

    assert response.status_code == 200

    data = response.json()

    assert "title" in data
    assert "link" in data
    assert "owner" in data
    assert "reputation" in data["owner"]


def test_lowest_views_endpoint():
    response = client.get("/api/stackoverflow/lowest-views")

    assert response.status_code == 200

    data = response.json()

    assert "title" in data
    assert "link" in data
    assert "view_count" in data

    assert isinstance(data["view_count"], int)


def test_oldest_newest_endpoint():
    response = client.get("/api/stackoverflow/oldest-newest")

    assert response.status_code == 200

    data = response.json()

    assert "oldest" in data
    assert "newest" in data

    assert "title" in data["oldest"]
    assert "creation_date" in data["oldest"]
    assert "link" in data["oldest"]

    assert "title" in data["newest"]
    assert "creation_date" in data["newest"]
    assert "link" in data["newest"]


def test_console_report_endpoint():
    response = client.get("/api/stackoverflow/console-report")

    assert response.status_code == 200

    data = response.json()

    assert "message" in data
    assert "printed" in data
    assert data["printed"] is True