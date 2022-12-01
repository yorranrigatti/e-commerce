from django.urls import path
from rest_framework_simplejwt import views as authview

from . import views

urlpatterns = [
    path("products/", views.ListCreateProductView.as_view()),
    path("products/<pk>/", views.RetrieveUpdateDestroyProductView.as_view())
]
