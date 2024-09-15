from django.contrib import admin
from .models import StudentHomeworkModel

class StudentHomeworkModelAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'topic_name', 'status', 'date')
    search_fields = ('subject_name', 'topic_name')
    list_filter = ('status', 'date')

admin.site.register(StudentHomeworkModel, StudentHomeworkModelAdmin)

