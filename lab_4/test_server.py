from server import Server
import requests


def test_put_labs():
    server = Server()
    server.run()
    payload = {'name': 'lab1'}
    response = requests.put('http://0.0.0.0:8080/labs', data=payload)
    assert response.status_code == 200

    # response = requests.get('https://api.example.com/movies')
    # assert response.status_code == 200
    # assert len(response.json()) > 0
