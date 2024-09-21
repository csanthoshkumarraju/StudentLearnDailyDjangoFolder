from django.contrib import admin
from .models import studentmonthlyplanmodel
# Register your models here.

class studentmonthlymodeladmin(admin.ModelAdmin):
    list_display = ('student_monthly_plan', 'monthly_status')
    search_fields = ('student_monthly_plan', 'monthly_status')
    list_filter = ('student_monthly_plan', 'monthly_status')

admin.site.register(studentmonthlyplanmodel, studentmonthlymodeladmin)