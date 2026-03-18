from django.db import models

class Attempt(models.Model):
    student = models.ForeignKey("handler.Student", on_delete=models.CASCADE)
    exam = models.ForeignKey("handler.Exam", on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_submitted = models.BooleanField(default=False)