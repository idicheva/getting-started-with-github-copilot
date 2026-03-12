def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "description" in payload["Chess Club"]
    assert "schedule" in payload["Chess Club"]
    assert "max_participants" in payload["Chess Club"]
    assert "participants" in payload["Chess Club"]


def test_get_activities_includes_seeded_participants(client):
    response = client.get("/activities")

    assert response.status_code == 200

    payload = response.json()
    assert "michael@mergington.edu" in payload["Chess Club"]["participants"]
    assert "grace@mergington.edu" in payload["Math Olympiad"]["participants"]
