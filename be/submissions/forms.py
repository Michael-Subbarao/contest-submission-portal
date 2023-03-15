from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('title', 'contest', 'author_name', 'author_bio', 'contact_email', 'content', 'genre')
