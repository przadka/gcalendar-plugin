def test_home(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
