from django.db import models

# Create your models here.
class Article(models.Model):
    fullurl = models.URLField()
    title = models.TextField()
    summary = models.TextField()
    full_text = models.TextField()

    def __str__(self):
        return self.title
