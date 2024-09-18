from django.contrib import admin
from .models import studentassignmentsmodel 

class studentassignmentsadmin(admin.ModelAdmin):  # Corrected class name
    list_display = ('assignment', 'status')
    search_fields = ('assignment', 'status')
    list_filter = ('assignment', 'status')

admin.site.register(studentassignmentsmodel, studentassignmentsadmin)  # Ensure consistency
