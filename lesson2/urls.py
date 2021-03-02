from django.urls import path
from . import views as simple_views

urlpatterns = [
    path('brands/', simple_views.car_brand_list_view),
    path('cars/', simple_views.car_list_view),
]