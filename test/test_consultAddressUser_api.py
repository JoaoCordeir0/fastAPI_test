import requests

def test_consultAddressUser_api():
    headers = {
        'User-Agent': 'request'
    }
    
    url_api = "http://127.0.0.1:8000/ConsultAddressUser/1"

    result = requests.get(
        url_api,       
        headers=headers
    )

    assert result.status_code == 200
