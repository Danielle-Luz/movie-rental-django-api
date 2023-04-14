from django.urls import path
from .views import MovieView, MovieInfoView, MovieOrderView

urlpatterns = [
    path("", MovieView.as_view()),
    path("<int:movie_id>/", MovieInfoView.as_view()),
    path("<int:movie_id>/orders/", MovieOrderView.as_view())
]
