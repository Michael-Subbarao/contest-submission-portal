from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from submissions.models import Submission, Contest, Genre
from submissions.forms import SubmissionForm
from .forms import UserRegistrationForm

def submission_list(request):
    submissions = Submission.objects.all()
    contests = Contest.objects.all()
    genres = Genre.objects.all()
    return render(request, 'submissions/submission_list.html', {'submissions': submissions, 'contests': contests, 'genres': genres})

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    return render(request, 'submissions/submission_detail.html', {'submission': submission})

def submission_create(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            submission.save()
            return redirect('submissions:submission_detail', pk=submission.pk)
    else:
        form = SubmissionForm()
    return render(request, 'submissions/submission_form.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('submissions:submission_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('submissions:submission_list')
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

