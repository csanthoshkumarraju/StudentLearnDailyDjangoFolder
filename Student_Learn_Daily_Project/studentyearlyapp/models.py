from django.db import models
from studentregisterapp.models import StudentRegistrationModel
# Create your models here.

class studentyearlyplan(models.Model):
      student = models.ForeignKey(StudentRegistrationModel,on_delete=models.CASCADE,null=True)
      yearly_plan = models.TextField(null=True)
      yealy_plan_status = models.CharField(max_length=500,null=True,default="To Do")

      def __str__(self) -> str:
            return self.yearly_plan
