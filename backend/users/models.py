from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYER = 'EMPLOYER', 'Employer'
        JOB_SEEKER = 'JOB_SEEKER', 'Job Seeker'
        ADMIN = 'ADMIN', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.JOB_SEEKER
    )

    def __str__(self):
        return f"{self.username} ({self.role})"