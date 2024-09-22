from django.contrib import admin
from .models import studentgoalsmodel
# Register your models here.

class studentgoalsmodeladmin(admin.ModelAdmin):
    list_display = ('goal', 'goal_status')
    search_fields = ('goal', 'goal_status')
    list_filter = ('goal', 'goal_status')

admin.site.register(studentgoalsmodel, studentgoalsmodeladmin)

