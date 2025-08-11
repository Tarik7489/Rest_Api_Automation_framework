def test_patch_post(api):
    res = api.patch("/posts/1", json={"title": "patched title"})
    assert res.status_code == 200
    assert res.json()["title"] == "patched title"
