from django.core.management import call_command
from django.urls import include, path
from rest_framework import serializers
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from browsable_router.meta import APIMetadata
from browsable_router.router import APIRouter


call_command("makemigrations")
call_command("migrate")


router = APIRouter()
router2 = APIRouter(name="route")
router3 = DefaultRouter()


class InputSerializer(serializers.Serializer):
    email = serializers.CharField()


class Viewset(ListModelMixin, CreateModelMixin, GenericViewSet):
    metadata_class = APIMetadata
    serializer_class = InputSerializer

    def get_queryset(self):
        return {}


class View(APIView):
    metadata_class = APIMetadata
    serializer_class = InputSerializer

    def get(self, request, *args, **kwargs):
        return Response()

    def post(self, request, *args, **kwargs):
        return Response()


router2.register(r"test1", Viewset, "route1test1")
router2.register(r"test2", View, "route1test2")
router3.register(r"test1", Viewset, "route2test1")
router.navigation_routes = {"route": router2, "plain": router3}


router.register(r"test1", Viewset, "test1")
router.register(r"test1/(?P<username>.+)", Viewset, "test1-username")
router.register(r"test2", View, "test2")
router.register(r"test2/(?P<username>\d+)", View, "test2-username", username=0)


urlpatterns = [
    path("", include(router.urls)),
]
