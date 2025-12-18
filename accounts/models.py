
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
 is_candidate = models.BooleanField(default=False)
 is_recruiter = models.BooleanField(default=False)
