def test_delete_post(api):
    res = api.delete("/posts/1")
    assert res.status_code == 200  # JSONPlaceholder always returns 200
