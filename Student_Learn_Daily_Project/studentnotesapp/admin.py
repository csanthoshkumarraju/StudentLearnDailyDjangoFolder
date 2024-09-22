from django.contrib import admin
from .models import studentnotesmodel
# Register your models here.
class studentnotesmodeladmin(admin.ModelAdmin):
    list_display = ('notes',)
    search_fields = ('notes',)
    list_filter = ('notes',)

admin.site.register(studentnotesmodel, studentnotesmodeladmin)