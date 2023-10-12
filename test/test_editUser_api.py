import requests

def test_editUser_api():
    headers = {
        'User-Agent': 'request'
    }
    
    url_api = "http://127.0.0.1:8000/EditUser"

    result = requests.put(
        url_api,
        json={
            "user_id": 1,
            "name": "Teste edição",
            "email": "teste@gmail.com",
            "password_hash": "teste1234"
        },
        headers=headers
    )

    assert result.status_code == 200
