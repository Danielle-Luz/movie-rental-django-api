from django.urls import path
from .views import UserView, UserInfoView
from rest_framework_simplejwt import views

urlpatterns = [
    path("", UserView.as_view()),
    path("login/", views.TokenObtainPairView.as_view()),
    path("<int:user_id>/", UserInfoView.as_view()),
]
