from django.urls import path, include
from rest_framework import routers

from . import views
from .views import JobViewSet


router = routers.DefaultRouter()
# REST API - при обращении методом GET https://somedomen/plan/jobs - получим список всех работ из БД
router.register('jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
