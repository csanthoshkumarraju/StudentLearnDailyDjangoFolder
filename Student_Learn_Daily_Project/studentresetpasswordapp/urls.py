from django.urls import path
from . import views

urlpatterns = [
    path('studentresetpassword/',views.student_reset_password,name='studentresetpassword')
]
