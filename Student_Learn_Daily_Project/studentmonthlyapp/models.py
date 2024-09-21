from django.db import models
from studentregisterapp.models import StudentRegistrationModel
# Create your models here.

class studentmonthlyplanmodel(models.Model):
    student = models.ForeignKey(StudentRegistrationModel, on_delete=models.CASCADE,null=True)
    student_monthly_plan = models.TextField(null=True)
    monthly_status = models.CharField(max_length=500,null=True,default="To Do")

    def __str__(self) -> str:
        return self.student_monthly_plan