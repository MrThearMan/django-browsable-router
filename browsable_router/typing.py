from typing import Any, Callable, Dict, List, Optional, Protocol, Set, Tuple, Type, Union

from django.urls import URLPattern, URLResolver
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin


__all__ = [
    "DictOrListOfDicts",
    "Any",
    "Dict",
    "Optional",
    "Protocol",
    "Set",
    "Type",
    "Union",
    "Callable",
    "Tuple",
    "UrlsType",
    "ViewType",
]


DictOrListOfDicts = Union[List[Dict[str, Any]], Dict[str, Any]]


class ViewProtocol(Protocol):
    allowed_methods: Set[str]

    def get_serializer(self, *args, **kwargs) -> Serializer:
        """Get serializer"""


UrlsType = List[Union[URLResolver, URLPattern]]
ViewType = Union[Type[APIView], Type[ViewSetMixin]]
