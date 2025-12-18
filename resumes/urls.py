
from django.urls import path
from . import views
urlpatterns=[
 path('upload/',views.upload),
 path('all/',views.all_resumes),
]
