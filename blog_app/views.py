from rest_framework import viewsets

from .models import Category, Post, Location
from .serializers import CategorySerializer, PostSerializer, LocationSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """ModelViewSet позволяет обрабатывать все CRUD запросы"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
