from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PostViewSet, LocationViewSet


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'location', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls))
]
