from django.urls import path
from .views import MovieView, MovieInfoView

urlpatterns = [
    path("", MovieView.as_view()),
    path("<int:movie_id>/", MovieInfoView.as_view()),
]
