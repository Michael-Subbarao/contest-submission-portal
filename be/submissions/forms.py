from django import forms
from .models import Submission, Contest, Genre

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['title', 'content', 'contest', 'genre']
