def test_post_car_returns_201_and_json(client):
    payload = {
        "make": "Ford",
        "model": "Fiesta",
        "year": 2018,
        "color": "Black",
    }

    response = client.post("/api/cars", json=payload)

    assert response.status_code == 201
    car = response.json()
    assert car["id"] > 0
    assert car["make"] == "Ford"
    assert car["model"] == "Fiesta"
    assert response.headers["location"] == f"/api/cars/{car['id']}"

def test_get_car_returns_200_and_json(client):
    payload1 = {
        "make": "Honda",
        "model": "Civic",
        "year": 1800,
        "color": "White"
    }
    response = client.post("/api/cars", json=payload1)
    
    assert response.status_code == 422
    
    get_response = client.get("api/cars")
    car_list = get_response.json()
    
    assert car_list == []
    
    