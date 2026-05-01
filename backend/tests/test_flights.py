from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_flights_summary_endpoint():
    response = client.get("/api/flights/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_vuelos" in data
    assert "total_aerolineas" in data
    assert "total_aeropuertos" in data
    assert "total_tipos_movimiento" in data


def test_all_flights_endpoint():
    response = client.get("/api/flights/all")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_flight = data[0]

    assert "nombre_aerolinea" in first_flight
    assert "nombre_aeropuerto" in first_flight
    assert "movimiento" in first_flight
    assert "dia" in first_flight


def test_top_airport_endpoint():
    response = client.get("/api/flights/top-airport")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_item = data[0]

    assert "nombre_aeropuerto" in first_item
    assert "total_movimientos" in first_item


def test_top_airline_endpoint():
    response = client.get("/api/flights/top-airline")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_item = data[0]

    assert "nombre_aerolinea" in first_item
    assert "total_vuelos" in first_item


def test_busiest_day_endpoint():
    response = client.get("/api/flights/busiest-day")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    first_item = data[0]

    assert "dia" in first_item
    assert "total_vuelos" in first_item


def test_airlines_more_than_two_flights_per_day_endpoint():
    response = client.get("/api/flights/airlines-more-than-two-flights-per-day")

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert "message" in data
    assert isinstance(data["results"], list)

    if len(data["results"]) > 0:
        first_item = data["results"][0]

        assert "nombre_aerolinea" in first_item
        assert "dia" in first_item
        assert "total_vuelos" in first_item
