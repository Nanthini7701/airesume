from django.db import models
from django.conf import settings

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to="resumes/")
    ats_score = models.IntegerField(default=0)

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    skills = models.JSONField(default=list, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
