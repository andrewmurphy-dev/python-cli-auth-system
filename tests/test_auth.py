from app.core.auth import sign_up_dict, sign_up_password, sign_up_username, login_structure


def test_sign_up_dict():
    result = sign_up_dict("andrew", "password")

    assert result == {
        "name": "andrew",
        "password": "password",
    }




def test_sign_up_password():
    result = sign_up_password("Barcelon1")

    assert result == 


#the problem is you cannot validate input !
#so better future design is to use a seperate validation from input ! 
#for example 

def validate_sign_up_password(password):
    password = password.strip()

    if not password:
        return None

    if len(password) < 6:
        return None

    if len(password) > 14:
        return None

    if " " in password:
        return None

    return password


# below is the test ! 

def test_validate_sign_up_password_accepts_valid_password():
    result = validate_sign_up_password("Barcelon1")

    assert result == "Barcelon1"





#another example with signup !

def sign_up_username(username):
    username = username.strip() 

    if not username:
        print("Error: username cannot be empty, try again!")
        return None
    
    if len(username) < 3:
        print("Error: username must be at least 3 characters long, try again!")
        return None
    

    if len(username) > 14:
        print("Error: username cannot be longer than 14 characters, try again!")
        return None
    
    if " " in username:
        print("Error: username cannot contain spaces, try again!")
        return None
    

    return username 


def test_sign_up_username():
    result = sign_up_username("Andrew")

    assert result == "Andrew"




def test_login_structure():
    result = login_structure("Andrew", "Secret12")


    assert result == {
        "name": "Andrew",
        "password": "Secret12",
    }







