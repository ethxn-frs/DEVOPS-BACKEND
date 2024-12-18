from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    summary = models.TextField()
