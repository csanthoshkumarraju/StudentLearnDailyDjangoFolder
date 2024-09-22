from django.db import models
from studentregisterapp.models import StudentRegistrationModel
# Create your models here.


class studentgoalsmodel(models.Model):
     student = models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE,null=True)
     goal = models.TextField(null=True)
     goal_status = models.CharField(max_length=500,null=True,default='To Do')

     def __str__(self) -> str:
          return self.goal