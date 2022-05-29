import datetime

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/quote")
    assert response.status_code == 200


def test_is_auto_date_today():
    response = client.get("/quote")
    request = "/quote/?date=" + datetime.date.today().isoformat()
    second_response = client.get(request)
    assert response.json() == second_response.json()