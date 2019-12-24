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
    ),
    path('controls/download-csv', 
        views.control_download, name='control_download'
    ),
    path('controls/export', 
        views.export_controls, name='control_export'
    ),
    path('controls/import', 
        views.import_controls, name='control_download'
    ),
    path('test', 
        views.testpage, name='testpage'
    ),
]