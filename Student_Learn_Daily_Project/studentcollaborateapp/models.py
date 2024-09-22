from django.db import models
from studentregisterapp.models import StudentRegistrationModel
# Create your models here.
class studentcollabaratemodel(models.Model):
      student = models.ForeignKey(StudentRegistrationModel,on_delete=models.CASCADE,null=True)
      message = models.TextField(null=True)
      date = models.DateTimeField(auto_now=False, auto_now_add=True)

      def __str__(self) -> str:
            return self.message