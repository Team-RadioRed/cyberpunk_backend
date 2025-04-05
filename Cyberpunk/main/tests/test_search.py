#import json
import pytest
from django.urls import reverse

@pytest.mark.parametrize("query", ["a", None])
def test_search_query(client, query):
    response = client.get(
        reverse('global_search'),
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
        reverse('global_search'),
        {"q": query, "collection": collection}
    )
    assert response.status_code == 404
    assert response.json() == {"message": "Некорректное название коллекции", "results": []}
