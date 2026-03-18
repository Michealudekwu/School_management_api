from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/')
    topic = models.ForeignKey("handler.Topic", on_delete=models.CASCADE)
    is_downloadable = models.BooleanField(default=True)