import requests

def test_registerUserAddress_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/RegisterUserAddress"

    result = requests.post(
        url_api,        
        json={
            "user_id": 1,
            "description": "Ao lado do posto de saúde",
            "postal_code": "13879002",
            "street": "Rua Atílio Tozatto",
            "complement": " ",
            "neighborhood": "Pedregulho",
            "city": "São João da Boa Vista",
            "state": "SP"
        },
        headers=headers
    )

    assert result.status_code == 200

