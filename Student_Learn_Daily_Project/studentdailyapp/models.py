from django.db import models
from studentregisterapp.models import StudentRegistrationModel


# Create your models here.
class studentdailymodel(models.Model):
    student = models.ForeignKey(StudentRegistrationModel,on_delete=models.CASCADE,null=True,related_name='dailyplans')
    daily_plan = models.TextField(null=True)
    daily_status = models.CharField(max_length=500,null=True,default="To do")

    def __str__(self) -> str:
        return self.daily_plan