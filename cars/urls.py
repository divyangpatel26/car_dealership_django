from django.urls import path
from . import views
from .views import add_car, edit_car, delete_car
from accounts import urls
urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:id>', views.car_detail, name='car_detail'),
    path('search', views.search, name='search'),
    path('add/', add_car, name='add_car'),
    path('edit/<int:car_id>/', edit_car, name='edit_car'),
     path('delete/<int:car_id>/', delete_car, name='delete_car'),
]
