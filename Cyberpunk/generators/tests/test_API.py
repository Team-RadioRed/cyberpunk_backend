import json
import pytest
from django.urls import reverse

@pytest.mark.parametrize("invalid_difficulty", ["abc", 5, 19, None])
def test_invalid_difficulty(client, invalid_difficulty):
    response = client.post(
        reverse('network_generator'),
        data=json.dumps({"difficulty": invalid_difficulty}),
        content_type="application/json"
    )
    assert response.status_code == 400
    assert response.json() == {'error': 'Некорректное значение сложности.'}

@pytest.mark.django_db
def test_valid_difficulty(client):
    response = client.post(
        reverse('network_generator'),
        data=json.dumps({"difficulty": 10}),
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "type" in response.json()