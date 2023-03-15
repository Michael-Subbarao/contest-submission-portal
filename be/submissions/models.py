from django.db import models
from django.contrib.auth import get_user_model

class Submission(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Genre(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField(default="No description provided.")

      def __str__(self):
        return self.name
