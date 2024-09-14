from django.contrib import admin
from .models import StudentRegistrationModel

@admin.register(StudentRegistrationModel)
class StudentRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


