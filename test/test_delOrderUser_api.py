import requests

def test_delOrderUser_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/DelOrderUser/1"

    result = requests.delete(
        url_api,        
        headers=headers
    )

    assert result.status_code == 200

