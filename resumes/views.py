
from django.shortcuts import render,redirect
from .models import Resume
from .utils import (
    extract_text, extract_email, extract_phone,
    extract_name, extract_skills, calculate_ats_score
)

def upload(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = request.FILES["file"]

        resume = Resume.objects.create(
            user=request.user,
            file=file
        )

        text = extract_text(resume.file.path)

        resume.name = extract_name(text)
        resume.email = extract_email(text)
        resume.phone = extract_phone(text)

        skills = extract_skills(text)
        resume.skills = skills
        resume.ats_score = calculate_ats_score(skills)

        resume.save()

    return redirect("candidate")
def all_resumes(request):
 r=Resume.objects.all()
 return render(request,'all_resumes.html',{'resumes':r})
