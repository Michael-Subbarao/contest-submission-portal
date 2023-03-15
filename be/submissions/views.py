from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from submissions.models import Submission, Contest, Genre
from submissions.forms import SubmissionForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView

def is_judge_or_superuser(user):
    return user.is_superuser or user.groups.filter(name='Judges').exists()

@user_passes_test(is_judge_or_superuser)
def submission_list(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions/submission_list.html', {'submissions': submissions})

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    return render(request, 'submissions/submission_detail.html', {'submission': submission})

class IsJudgeMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Judges').exists()

@login_required
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
