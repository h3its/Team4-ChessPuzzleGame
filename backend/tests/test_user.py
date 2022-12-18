import base64

def test_create_user(client):
    user = { 'email': 'foo1@bar.com', 'password': 'foo'}
    resp = client.post('/users', json=user)
    assert resp.status_code == 200

def test_high_score(client, sample_user):
    auth = auth_header(sample_user.email, 'password')
    score = { 'score': 100, 'level': 50 }
    resp = client.post('/scores', headers=auth, json=score)
    assert resp.status_code == 200

def test_get_user(client, sample_user):
    auth = auth_header(sample_user.email, 'password')
    resp = client.get('/user', headers=auth)
    assert resp.status_code == 200

def test_get_user_unauthorized(client, sample_user):
    auth = auth_header(sample_user.email, 'blah')
    resp = client.get('/user', headers=auth)
    assert resp.status_code == 401

def test_leaders(client, sample_user):
    auth = auth_header(sample_user.email, 'password')
    score = { 'score': 100, 'level': 50 }
    client.post('/scores', headers=auth, json=score)
    resp = client.get('/users/leaders?level=50', headers=auth)
    print(resp.json)
    assert resp.status_code == 200

def auth_header(email, password):
    auth_string = f"{email}:{password}"
    auth_ascii = auth_string.encode('ascii')
    auth_64 = base64.b64encode(auth_ascii)
    auth = { 'Authorization': "Basic " + auth_64.decode('ascii')}
    return auth

