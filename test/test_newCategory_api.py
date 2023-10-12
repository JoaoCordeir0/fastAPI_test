import requests

def test_newCategory_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/NewCategory"

    result = requests.post(
        url_api,        
        json={
            "name": "Esportes"
        },
        headers=headers
    )

    assert result.status_code == 200

