def test_get_post(api):
    res = api.get("/posts/1")
    assert res.status_code == 200

    response = res.json()

    assert response["id"] == 1
