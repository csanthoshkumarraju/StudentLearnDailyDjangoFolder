from django.db import models
from studentregisterapp.models import StudentRegistrationModel 
# Create your models here.

class studentassignmentsmodel(models.Model):
    student = models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE,related_name='assignments',null=True)
    assignment = models.TextField(null=True)
    status = models.CharField(max_length=500,null=True,default="To Do")

    def __str__(self):
        return self.assignment
    