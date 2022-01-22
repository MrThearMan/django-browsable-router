# Django Browsable Router

[![Coverage Status][coverage-badge]][coverage]
[![GitHub Workflow Status][status-badge]][status]
[![PyPI][pypi-badge]][pypi]
[![GitHub][licence-badge]][licence]
[![GitHub Last Commit][repo-badge]][repo]
[![GitHub Issues][issues-badge]][issues]
[![Python Version][version-badge]][pypi]

```shell
pip install django-browsable-router
```

---

**Documentation**: [https://mrthearman.github.io/django-browsable-router/](https://mrthearman.github.io/django-browsable-router/)

**Source Code**: [https://github.com/MrThearMan/django-browsable-router/](https://github.com/MrThearMan/django-browsable-router/)

---

A Django Restframework router that can show APIViews and include other routers as navigable urls in the root view.

```python
from browsable_router import APIRouter
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

class TestView(APIView):
  ...

class TestViewSet(ViewSet):
  ...

router_1 = APIRouter(name="other_routes", docstring="These are under a different route.")
router_1.register(r"view-1", TestView.as_view(), "view_1")
router_1.register(r"view-2", TestViewSet.as_view(), "view_2")

router_2 = APIRouter()
router_2.register(r"view-3", TestView.as_view(), "view_3")
router_2.navigation_routes = {
    "route": router_1,
}

urlpatterns = [
    path("api/", include(router_2.urls))
]
```

Resulting browsable API:
```python
#   API Root:
#   """API root."""
#
#   "route":    "/api/route/"
#   "view-3":   "/api/view-3/"
#
#   Other Routes:
#   """These are under a different route."""
#
#   "view-1":    "/api/route/view-1/"
#   "view-2":    "/api/route/view-2/"
```

---

# Additional stuff:

### ApiMetadata
This metadata class is enabled by default on BaseAPIView, and it will allow you to document your views automatically.
Basically, it reads the InputSerializers fields as input, and the OutputSerializer fields as the output for each HTTP method for that view.
You can then make a OPTIONS request to the view endpoint and get a JSON Schema-ish representation of the input and output for that endpoint.

### SerializerAsOutputMetadata
This metadata class works like APIMetadata class, but is intended for the generic views that come with django rest framework.
It assumes that the endpoint takes no arguments and returns the method serializers fields as output.

### BlockSchemaAccess
This is a permission class that can be used to block access to OPTIONS schema in production (DEBUG=False).


[coverage-badge]: https://coveralls.io/repos/github/MrThearMan/django-browsable-router/badge.svg?branch=main
[status-badge]: https://img.shields.io/github/workflow/status/MrThearMan/django-browsable-router/Tests
[pypi-badge]: https://img.shields.io/pypi/v/django-browsable-router
[licence-badge]: https://img.shields.io/github/license/MrThearMan/django-browsable-router
[repo-badge]: https://img.shields.io/github/last-commit/MrThearMan/django-browsable-router
[issues-badge]: https://img.shields.io/github/issues-raw/MrThearMan/django-browsable-router
[version-badge]: https://img.shields.io/pypi/pyversions/django-browsable-router

[coverage]: https://coveralls.io/github/MrThearMan/django-browsable-router?branch=main
[status]: https://github.com/MrThearMan/django-browsable-router/actions/workflows/main.yml
[pypi]: https://pypi.org/project/django-browsable-router
[licence]: https://github.com/MrThearMan/django-browsable-router/blob/main/LICENSE
[repo]: https://github.com/MrThearMan/django-browsable-router/commits/main
[issues]: https://github.com/MrThearMan/django-browsable-router/issues
