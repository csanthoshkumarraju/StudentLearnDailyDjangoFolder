from django.contrib import admin
from .models import studentyearlyplan
# Register your models here.

class studentyearlyplanadmin(admin.ModelAdmin):
    list_display = ('yearly_plan', 'yealy_plan_status')
    search_fields = ('yearly_plan', 'yealy_plan_status')
    list_filter = ('yearly_plan', 'yealy_plan_status')

admin.site.register(studentyearlyplan, studentyearlyplanadmin)
