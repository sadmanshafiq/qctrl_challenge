# urls.py contains routers and import export path to route for usage

from django.urls import path, include
from . import views
from rest_framework import routers

#used routers to simplify controls api HTTP requests
router = routers.DefaultRouter()
router.register('controls', views.BaseViewSet)

urlpatterns = [
    path('', #opens /controls/ with ModelView
        include(router.urls), 
        name="controls-page"
        ),
    path('controls/export',  #links to export.html
        views.export_controls, name='control_export'
        ),
    path('controls/import',  #links to import.html 
        views.import_controls, name='control_import'
        ),
]