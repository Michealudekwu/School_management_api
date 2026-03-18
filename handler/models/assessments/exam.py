from django.db import models

class Exam(models.Model):
    EXAM_TYPE = (
        ('practice', 'Practice'),
        ('test', 'Test'),
        ('exam', 'Exam')
    )
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE)
    course = models.ForeignKey("handler.Course", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration_mins = models.IntegerField()
    total_marks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)