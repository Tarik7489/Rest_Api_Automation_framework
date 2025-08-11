<<<<<<< HEAD

# Test
=======
>>>>>>> 099fbd400b08e47ded5b43839341d9f33b056d38
def test_get_post(api):
    res = api.get("/posts/1")
    assert res.status_code == 200

    response = res.json()

    assert response["id"] == 1
