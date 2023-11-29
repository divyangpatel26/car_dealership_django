# urls.py
from django.urls import path
from . import views
from .views import edit_profile, inquiries

urlpatterns = [
    path('register/', views.register, name='register'),
    path('seller_registration/', views.seller_registration, name='seller_registration'),
    path('buyer_registration/', views.buyer_registration, name='buyer_registration'),
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_user, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('inquiries/', inquiries, name='inquiries'),
]
