from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, 
    CategoryViewSet, 
    JobViewSet, 
    ApplicationViewSet
)

# DRF Router එක සාදා ViewSets ලියාපදිංචි කිරීම
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]