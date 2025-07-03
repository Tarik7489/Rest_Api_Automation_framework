from data.payloads import update_post_payload

def test_update_post_put(api):
    res = api.put("/posts/1", json=update_post_payload())
    assert res.status_code == 200
    assert res.json()["title"] == "Updated Monster Title"
