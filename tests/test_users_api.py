from fastapi.testclient import TestClient
from app.main_api import app



client = TestClient(app)

#so lets test GET / users 


#so the function we call is the response function 



def test_get_users_response_list():
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    


#so here we can test the endpoint response resturns successful data! 
#response

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



#so lets try test router.post("/users")


def test_post_users_response_format():
    response = client.post("/users")
    data = response.json()

    assert response.status_code == 200

    assert set(data.keys()) == {"message", "user"}

    assert isinstance(data["message"], str)
    assert isinstance(data["user"], new_user)


    #see how can we check the type for new_user 
    #so new_user is a dict


    #two issues 


    #1

    #your request exprects a json body ! 

    #so we need to do this ! 

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


    

