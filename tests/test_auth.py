from app.core.auth import sign_up_dict,login_structure


def test_sign_up_dict():
    result = sign_up_dict("andrew", "password")

    assert result == {
        "name": "andrew",
        "password": "password",
    }




def test_login_structure():
    result = login_structure("Andrew", "Secret12")


    assert result == {
        "name": "Andrew",
        "password": "Secret12",
    }







