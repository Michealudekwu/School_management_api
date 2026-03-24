from django.db import models
from .user import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    department = models.ForeignKey("handler.Department", on_delete=models.CASCADE)
    level = models.ForeignKey("handler.Level", on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=50, unique=True)