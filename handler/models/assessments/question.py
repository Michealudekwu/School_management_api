from django.db import models

class Question(models.Model):
    QUESTION_TYPE = (
        ('mcq', 'Multiple Choice'),
        ('true_false', 'True/False')
    )
    exam = models.ForeignKey("handler.Exam", on_delete=models.CASCADE)
    question_text = models.TextField()
    questin_type = models.CharField(max_length=20, choices=QUESTION_TYPE)
    mark = models.IntegerField()