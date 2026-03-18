from django.db import models
from .user import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    department = models.ForeignKey("handler.Department", on_delete=models.SET_NULL, null=True)
    staff_id = models.CharField(max_length=50, unique=True)
    level = models.ManyToManyField("handler.Level", related_name='teachers') 