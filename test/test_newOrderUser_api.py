import requests

def test_newOrderUser_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/NewOrderUser"

    result = requests.post(
        url_api,        
        json={
            "user_id": 2,
            "status": "Pendente",
            "order_date": "2023-04-16",
            "products": {
                "product_id": [1, 2],
                "quantity": [1, 2],
                "price": [20.00, 30.00]
            },
            "address_id": 1
        },
        headers=headers
    )

    assert result.status_code == 200

