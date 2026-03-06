from django.urls import path
from .views import login_page,register_user

urlpatterns = [
    path('', login_page, name='login'),
    path('register/', register_user),
]
