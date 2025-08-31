from django.urls import path
from .views import TepListByRegionView

urlpatterns = [
    path('teps/<int:region_id>/', TepListByRegionView.as_view(), name='tep-list-by-region'),
]