from app import app
 
def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, CI/CD!" in response.data

def test_add_numbers_success():
    client = app.test_client()
    response = client.get("/add?a=5&b=7")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 12

 
def test_subtract_numbers_success():
    client = app.test_client()
    response = client.get("/subtract?a=10&b=3")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 7

def test_multiply_numbers_success():
    client = app.test_client()
    response = client.get("/multiply?a=6&b=5")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 30

def test_divide_numbers_success():
    client = app.test_client()
    response = client.get("/divide?a=6&b=3")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 2

 
 
 