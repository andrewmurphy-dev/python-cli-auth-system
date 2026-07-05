from fastapi.testclient import TestClient
from app.main_api import app



client = TestClient(app)



def test_get_users_response_list():
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    



def test_get_users_response_format():
    response = client.get("/users")
    users = response.json()

    assert response.status_code == 200

    for user in users:
        assert set(user.keys()) == {"id", "name", "password", "created_at"}
        assert isinstance(user["id"], int)
        assert isinstance(user["name"], str)
        assert isinstance(user["password"], str)
        assert isinstance(user["created_at"], str)



def test_post_users_response_format():
    response = client.post("/users", json={
        "name": "testuser",
        "password": "secret134"
    })

    data = response.json()

    assert response.status_code == 200


    assert set(data.keys()) == {"message", "user"}
    assert isinstance(data["message"], str)
    assert isinstance(data["user"], dict)

    user = data["user"]

    assert set(user.keys()) == {"id", "name", "password", "created_at"}
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["password"], str)
    assert isinstance(user["password"], str)






def test_post_request_login():
    response = client.post("/login", json={
        "name": "testlogin",
        "password": "passwordlogin"
    })

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data["message"], str)



