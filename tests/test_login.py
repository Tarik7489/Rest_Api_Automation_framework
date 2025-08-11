from data.payloads import login_payload


def test_login_get_profile_info(baseUrl):
    # Step 1: Login and get access token
    payload = login_payload()
    login_res = baseUrl.post("/api/v1/auth/login", json=payload)
    token = login_res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # Step 2: Get profile info
    profile_res = baseUrl.get("/api/v1/auth/profile", headers=headers)
    assert profile_res.status_code == 200

    profile = profile_res.json()
    print("👤 Profile Response:", profile)

    # ✅ Assertions
    assert profile["id"] == 1, "User ID should be 1"
    assert profile["email"] == "john@mail.com", "Email doesn't match"
    assert profile["password"] == "changeme", "Password doesn't match"
    assert profile["name"] == "Jhon", "Name doesn't match"
    assert profile["role"] == "customer", "Role should be customer"
    assert profile["avatar"].startswith("https://"), "Avatar URL should be valid"
