from django.db import models
from studentregisterapp.models import StudentRegistrationModel
# Create your models here.
class studentnotesmodel(models.Model):
    student = models.ForeignKey(StudentRegistrationModel,on_delete=models.CASCADE,null=True)
    notes = models.TextField(null=True)

    def __str__(self):
        return self.notes
    
