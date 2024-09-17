# from django.contrib import admin
# from .models import StudentRegistrationModel

# @admin.register(StudentRegistrationModel)
# class StudentRegistrationModelAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StudentRegistrationModel

class UserAdmin(BaseUserAdmin):
    model = StudentRegistrationModel
    # Specify the fields to display in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    
    # The fields to use when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    
    # The fields to use when editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

admin.site.register(StudentRegistrationModel, UserAdmin)

