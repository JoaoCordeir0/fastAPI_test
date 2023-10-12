import requests

def test_newUser_api():
    headers = {
        'User-Agent': 'request'
    }
    
    url_api = "http://127.0.0.1:8000/NewUser"

    result = requests.post(
        url_api,
        json={
            "name": "João Victor Cordeiro",
            "email": "joaocordeiro2134@gmail.com",
            "password_hash": "joao1234"
        },
        headers=headers
    )

    assert result.status_code == 200
