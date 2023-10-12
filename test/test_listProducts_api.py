import requests

def test_listProducts_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/ListProducts"

    result = requests.get(
        url_api,        
        headers=headers
    )

    assert result.status_code == 200

