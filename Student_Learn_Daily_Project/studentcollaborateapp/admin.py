from django.contrib import admin
from .models import studentcollabaratemodel
# Register your models here.
class  studentcollabaratemodeladmin(admin.ModelAdmin):
    list_display = ('message', 'date')
    search_fields = ('message', 'date')
    list_filter = ('message', 'date')

admin.site.register(studentcollabaratemodel, studentcollabaratemodeladmin)