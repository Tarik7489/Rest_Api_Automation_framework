from data.payloads import create_post_payload

def test_create_post(api):
    payload = create_post_payload()
    res = api.post("/posts", json=payload)

    assert res.status_code == 201

    response = res.json()
    # ✅ What it means:
    # res is the HTTP response object returned by requests.post() (or .get(), .put(), etc.).

    # res.json() is a built-in Requests method that converts the JSON response body into a Python dictionary.

    # So, response = res.json() just stores that dictionary into a variable named response.

    # ✅ Top-level fields
    assert response["title"] == "Monster"
    assert response["userId"] == 1
    assert response["category"] == "QA Automation"
    assert response["status"] == "draft"
    assert response["priority"] == "high"
    assert response["createdAt"] == "2025-07-03T10:00:00Z"
    assert response["updatedAt"] is None
    assert response["tags"] == ["automation", "python", "test"]

    # ✅ Nested metadata object
    assert "metadata" in response
    assert response["metadata"]["os"] == "Windows"
    assert response["metadata"]["browser"] == "Chrome"
    assert response["metadata"]["execution_time"] == "2s"

    # ✅ Comments should be an empty list
    assert "comments" in response
    assert isinstance(response["comments"], list)
    assert len(response["comments"]) == 0
