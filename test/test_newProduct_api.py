import requests

def test_newProduct_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/NewProduct"

    result = requests.post(
        url_api,        
        json={
            "name": "Chuteira de futebol",
            "description": "Society",
            "price": 250.00,
            "category_id": 1
        },
        headers=headers
    )

    assert result.status_code == 200

