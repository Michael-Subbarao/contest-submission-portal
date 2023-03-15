from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from submissions.models import Submission, Contest, Genre
from submissions.forms import SubmissionForm

def submission_list(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions/submission_list.html', {'submissions': submissions})

def submission_detail(request, pk):
    submission = get_object_or_404(Submission, pk=pk)
    return render(request, 'submissions/submission_detail.html', {'submission': submission})

@login_required
def submission_create(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect('submissions:submission_detail', pk=submission.pk)
    else:
        form = SubmissionForm()
    return render(request, 'submissions/submission_form.html', {'form': form})
