
from django.urls import path
from . import views
urlpatterns=[
 path('',views.login_view,name='login'),
 path('signup/candidate/',views.signup_candidate),
 path('signup/recruiter/',views.signup_recruiter),
 path('logout/',views.logout_view),
 path('candidate/',views.candidate_dash,name='candidate'),
 path('recruiter/',views.recruiter_dash,name='recruiter'),
]
