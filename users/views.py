from rest_framework import generics

from users.permissions import isSuperuserOrOwner, isSuperuser
from users.serializers import UserSerializer

from .models import User


class ListUserView(generics.ListAPIView):
    permission_classes = [isSuperuser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [isSuperuserOrOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
