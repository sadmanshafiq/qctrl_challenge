# urls.py contains routers and import export path to route for usage

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('controls', views.BaseViewSet)


urlpatterns = [
    path('', include(router.urls), name="controls-page"),
    path('controls/export', 
        views.export_controls, name='control_export'
    ),
    path('controls/import', 
        views.import_controls, name='control_import'
    ),
]