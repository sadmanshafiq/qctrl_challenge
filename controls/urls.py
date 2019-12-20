from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('controls', views.BaseViewSet)

urlpatterns = [
   path('', include(router.urls), name="controls-all")
]