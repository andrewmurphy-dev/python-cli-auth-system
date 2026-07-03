from fastapi.testclient import TestClient 
from app.main_api import app 




client = TestClient(app)

#so lets test GET / users 


#so the function we call is the response function 



def test_get_users_response_list():
    response = client.get("/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    


#you also need to check if the response from the endpoint is sending the correct format 
#I expect GET /users to return a list.



