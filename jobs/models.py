from django.db import models
from django.conf import settings

# 1. Company Model 
class Company(models.Model):
    employer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# 2. Category Model 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 3. Job Model 
class Job(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='jobs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.title

# 4. Application Model 
class Application(models.Model):
    STATUS_CHOICES = (
        ('APPLIED', 'Applied'),
        ('REVIEWED', 'Reviewed'),
        ('REJECTED', 'Rejected'),
        ('ACCEPTED', 'Accepted'),
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"