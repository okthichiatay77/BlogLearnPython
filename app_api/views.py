from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ServerImageSerializer
from my_app.models import ServerImages


class ServerImageView(viewsets.ModelViewSet):
    queryset = ServerImages.objects.all()
    serializer_class = ServerImageSerializer
