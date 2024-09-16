# from django.db import models
# from django.core.validators import MinLengthValidator
# from django.core.exceptions import ValidationError

# class StudentRegistrationModel(models.Model):
#     first_name = models.CharField(max_length=100,null=True)
#     last_name = models.CharField(max_length=100,null=True)
#     email = models.EmailField(unique=True,null=True)
#     password = models.CharField(max_length=100,null=True)
#     confirm_password = models.CharField(max_length=100,null=True)

#     def clean(self):
#         if self.password != self.confirm_password:
#             raise ValidationError("Passwords do not match")

#     def save(self, *args, **kwargs):
#         self.clean()
#         super().save(*args, **kwargs)


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models
# from django.utils import timezone

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

# class StudentRegistrationModel(AbstractBaseUser):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)  # max_length should be 128 for hashed passwords

#     # Required fields for AbstractBaseUser
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)  # Required for admin access

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']

#     def __str__(self):
#         return self.email


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class StudentRegistrationModel(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # max_length should be 128 for hashed passwords

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for admin access

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

