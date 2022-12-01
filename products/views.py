from rest_framework import generics
from users.permissions import isSuperuser, isSuperUserOrSafeMethod

from .models import Product
from .serializers import ProductSerializer


class ListCreateProductView(generics.ListCreateAPIView):
    permission_classes = [isSuperUserOrSafeMethod]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveUpdateDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperUserOrSafeMethod]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

