from django.db import models

class Option(models.Model):
    question = models.ForeignKey("handler.Question", related_name='options', on_delete=models.CASCADE)
    option_value = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)