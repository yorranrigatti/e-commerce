from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("users/login/", authview.TokenObtainPairView.as_view()),
    path("users/", views.CreateUserView.as_view()),
    path("users/list/", views.ListUserView.as_view()),
    path("users/<pk>/", views.RetrieveUpdateDestroyUserView.as_view())
]
