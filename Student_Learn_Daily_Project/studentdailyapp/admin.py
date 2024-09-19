from django.contrib import admin
from .models import studentdailymodel
# Register your models here.

class  studentdailymodeladmin(admin.ModelAdmin):
    list_display = ('daily_plan', 'daily_status')
    search_fields = ('daily_plan', 'daily_status')
    list_filter = ('daily_plan', 'daily_status')

admin.site.register(studentdailymodel, studentdailymodeladmin)