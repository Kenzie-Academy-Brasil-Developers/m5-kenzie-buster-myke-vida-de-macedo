from django.urls import path

from .views import UserView, UserIdView, LoginJWTView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginJWTView.as_view()),  
    path("users/<user_id>/", UserIdView.as_view()),  
]
    