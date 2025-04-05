#import json
import pytest
from django.urls import reverse


@pytest.mark.parametrize("query", ["a", None])
def test_search_query(client, query):
    response = client.get(
        reverse('main:global_search'),
        {"q": query}
    )
    assert response.status_code == 400
    assert response.json() == {"message": "Некорректный запрос", "results": []}


@pytest.mark.django_db
@pytest.mark.parametrize("query, collection", [
    ("cyber", "not_existing_collection"),
])
def test_search_collection(client, query, collection):
    response = client.get(
        reverse('main:global_search'),
        {"q": query, "collection": collection}
    )
    assert response.status_code == 404
    assert response.json() == {"message": "Некорректное название коллекции", "results": []}


@pytest.mark.django_db
def test_search_valid_query_and_collection(client):
    response = client.get(
        reverse("main:global_search"),
        {"q": "chip", "collection": "cyberware"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["results"]  # Проверяем, что результаты не пустые
    
    found = False
    for item in data["results"]:
        english_name = item.get("name", {}).get("en", "").lower()
        if "chip" in english_name:
            found = True
            break
    
    assert found, "No items with 'chip' in English name found"
