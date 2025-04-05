import pytest
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize("url_name", [
    "references:weapons_list",
    "references:programs_list",
    "references:cyberware_list",
    "references:transport_list",
    "references:roles_list",
])
def test_collection_endpoints(client, url_name):
    response = client.get(reverse(url_name))

    assert response.status_code == 200
    json_data = response.json()
    assert json_data  # просто убеждаемся, что есть какой-то контент