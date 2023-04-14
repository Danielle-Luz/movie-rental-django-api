from django.urls import path
from .views import UserView
from rest_framework_simplejwt import views

urlpatterns = [
    path("", UserView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
]
