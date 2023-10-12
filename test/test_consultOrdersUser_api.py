import requests

def test_consultOrdersUser_api():
    headers = {
        'User-Agent': 'request'
    }

    url_api = "http://127.0.0.1:8000/ConsultOrdersUser"

    result = requests.post(
        url_api,        
        json={
            "user_id": 1,
            "start_date": "2023-04-15",
            "end_date": "2023-04-19"
        },
        headers=headers
    )

    assert result.status_code == 200

