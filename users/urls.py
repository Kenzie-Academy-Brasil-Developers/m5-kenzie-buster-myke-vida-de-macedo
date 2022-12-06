from django.urls import path

from .views import UserView
from .views import LoginJWTView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginJWTView.as_view()),  
]
    