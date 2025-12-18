from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from resumes.models import Resume
from .forms import CustomUserCreationForm

User = get_user_model()


# =========================
# SIGNUP VIEWS
# =========================

def signup_candidate(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_candidate = True
            user.is_recruiter = False
            user.save()
            login(request, user)
            return redirect('candidate')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def signup_recruiter(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_recruiter = True
            user.is_candidate = False
            user.save()
            login(request, user)
            return redirect('recruiter')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


# =========================
# LOGIN / LOGOUT
# =========================

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # ✅ ROLE-BASED REDIRECT
            if user.is_candidate:
                return redirect('candidate')
            elif user.is_recruiter:
                return redirect('recruiter')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# DASHBOARDS
# =========================

def candidate_dash(request):
    if not request.user.is_authenticated or not request.user.is_candidate:
        return redirect('login')

    resume = Resume.objects.filter(user=request.user).order_by('-id').first()

    return render(request, 'candidate.html', {
        'ats_score': resume.ats_score if resume else None,
        'skills': resume.skills if resume else [],
        'jobs': []
    })

def recruiter_dash(request):
    if not request.user.is_authenticated or not request.user.is_recruiter:
        return redirect('login')
    return render(request, 'recruiter.html')
