from django.urls import path

from .views import MovieView, MovieIdView, MovieOrderIdView

urlpatterns = [
    path("movies/", MovieView.as_view() ),
    path("movies/<movie_id>/", MovieIdView.as_view() ),
    path("movies/<movie_id>/orders/", MovieOrderIdView.as_view() )
]