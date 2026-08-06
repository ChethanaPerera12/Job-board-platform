from rest_framework import serializers
from .models import Company, Category, Job, Application

# 1. Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# 2. Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ['employer']  # Request employer user will be set automatically

# 3. Job Serializer
class JobSerializer(serializers.ModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Job
        fields = '__all__'

# 4. Application Serializer
class ApplicationSerializer(serializers.ModelSerializer):
    applicant_username = serializers.ReadOnlyField(source='applicant.username')
    job_title = serializers.ReadOnlyField(source='job.title')

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applicant']  # Apply user