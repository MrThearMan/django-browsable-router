import pytest
from django.http import HttpResponse


@pytest.mark.django_db
def test_test1_view_metadata(client):
    result: HttpResponse = client.options("/test1/", follow=True, content_type="application/json")
    content = result.json()
    expected = {
        "name": "Viewset List",
        "description": "",
        "renders": ["application/json", "text/html"],
        "parses": ["application/json", "application/x-www-form-urlencoded", "multipart/form-data"],
        "actions": {
            "GET": {"input": {"email": {"type": "string", "required": True}}, "exceptions": {}},
            "POST": {"input": {"email": {"type": "string", "required": True}}, "exceptions": {}},
        },
    }

    assert content == expected


@pytest.mark.django_db
def test_test2_view_metadata(client):
    result: HttpResponse = client.options("/test2/", follow=True, content_type="application/json")
    content = result.json()
    expected = {
        "name": "View",
        "description": "",
        "renders": ["application/json", "text/html"],
        "parses": ["application/json", "application/x-www-form-urlencoded", "multipart/form-data"],
        "actions": {
            "GET": {"input": {"email": {"type": "string", "required": True}}, "exceptions": {}},
            "POST": {"input": {"email": {"type": "string", "required": True}}, "exceptions": {}},
        },
    }

    assert content == expected
