from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        EMPLOYER = 'EMPLOYER', 'Employer'
        JOB_SEEKER = 'JOB_SEEKER', 'Job Seeker'

    base_role = Role.JOB_SEEKER

    role = models.CharField(max_role_length := 20, choices=Role.choices, default=base_role) 