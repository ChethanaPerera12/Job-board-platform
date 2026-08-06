from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Company, Category, Job, Application
from .serializers import (
    CompanySerializer, 
    CategorySerializer, 
    JobSerializer, 
    ApplicationSerializer
)

# 1. Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 2. Company ViewSet
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def perform_create(self, serializer):
        # Company එක සාදන විට employer ලෙස ලොග් වී සිටින user ස්වයංක්‍රීයව එකතු වේ
        serializer.save(employer=self.request.user)

# 3. Job ViewSet
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# 4. Application ViewSet
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        # Application එක දාන විට applicant ලෙස ලොග් වී සිටින user ස්වයංක්‍රීයව එකතු වේ
        serializer.save(applicant=self.request.user)
