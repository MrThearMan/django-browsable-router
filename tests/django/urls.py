try:
    from django.urls import re_path
except ImportError:
    from django.conf.urls import url as re_path

from rest_framework import serializers


urlpatterns = []
