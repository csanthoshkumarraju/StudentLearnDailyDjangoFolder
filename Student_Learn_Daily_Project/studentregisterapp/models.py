from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

class StudentRegistrationModel(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=100,null=True)
    confirm_password = models.CharField(max_length=100,null=True)

    def clean(self):
        if self.password != self.confirm_password:
            raise ValidationError("Passwords do not match")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
