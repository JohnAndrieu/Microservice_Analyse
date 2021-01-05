# src/tests/app/test_main.py

import string

def test_csv(client):
    response = client.get('/results_analyses/csv')
    assert response.status_code == 200
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "Done"

def test_data(client):
    response = client.get('/data')
    assert response.status_code == 200
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert all(c in string.printable for c in result["message"])