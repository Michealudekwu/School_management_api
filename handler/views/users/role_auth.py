from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.auth.get('role') == 'student'

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.auth.get('role') == 'teacher'
    
class IsMe(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.username == "sk")