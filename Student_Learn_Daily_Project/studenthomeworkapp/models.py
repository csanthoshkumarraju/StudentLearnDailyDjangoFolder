from django.db import models
from studentregisterapp.models import StudentRegistrationModel  # Import the StudentRegistrationModel

class StudentHomeworkModel(models.Model):
    student = models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE, related_name='homeworks',null=True)
    subject_name = models.TextField(max_length=1000,null=True)
    topic_name = models.TextField(max_length=1000,null=True)
    status = models.CharField(max_length=50, default="To do",null=True)
    date = models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.subject_name} - {self.topic_name}"

