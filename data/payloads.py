def create_post_payload():
    return {
        "title": "Monster",
        "body": "This is a test post body for creating a new post. It should be detailed.",
        "userId": 1,
        "tags": ["automation", "python", "test"],
        "status": "draft",
        "category": "QA Automation",
        "priority": "high",
        "createdAt": "2025-07-03T10:00:00Z",
        "updatedAt": None,
        "metadata": {
            "os": "Windows",
            "browser": "Chrome",
            "execution_time": "2s"
        },
        "comments": []
    }

def update_post_payload():
    return {
        "id": 1,
        "title": "Updated Monster Title",
        "body": "This is an updated post body with extended content and structure.",
        "userId": 1,
        "tags": ["automation", "updated", "post"],
        "status": "published",
        "category": "Regression Testing",
        "priority": "medium",
        "createdAt": "2025-07-01T08:30:00Z",
        "updatedAt": "2025-07-03T11:00:00Z",
        "metadata": {
            "os": "Linux",
            "browser": "Firefox",
            "execution_time": "1.5s"
        },
        "comments": [
            {
                "user": "tarik.qa",
                "message": "Looks good!",
                "timestamp": "2025-07-03T11:01:00Z"
            }
        ]
    }

def login_payload():
    return {

            "email": "john@mail.com",
            "password": "changeme"
        }
