from django.db import models

class Course(models.Model):
    SEMESTER_CHOICES = [
        ('FIRST', 'First Semester'),
        ('SECOND', 'Second Semester')
    ]
    code = models.CharField(max_length=15, unique=True)
    semester = models.CharField(max_length=30, choices= SEMESTER_CHOICES)
    title = models.CharField(max_length=100)
    level = models.ForeignKey("handler.Level", on_delete=models.CASCADE)
    department = models.ForeignKey("handler.Department", on_delete=models.CASCADE)
    teacher = models.ForeignKey("handler.Teacher", on_delete=models.SET_NULL, null=True, blank=True)