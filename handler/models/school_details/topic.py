from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    course = models.ForeignKey("handler.Course", on_delete=models.CASCADE)