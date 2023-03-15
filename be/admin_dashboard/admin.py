from django.contrib import admin
from submissions.models import Contest, Genre, Submission

admin.site.register(Contest)
admin.site.register(Genre)
admin.site.register(Submission)
