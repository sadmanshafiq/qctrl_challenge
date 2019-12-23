from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('controls', views.BaseViewSet)


urlpatterns = [
   path('', include(router.urls), name="controls-page"),
   path('api/v1/controls/<int:pk>/',
        views.get_delete_update_control,
        name='get_delete_update_control'
    ),
    path('api/v1/controls/',
        views.get_post_control,
        name='get_post_control'
    )
]