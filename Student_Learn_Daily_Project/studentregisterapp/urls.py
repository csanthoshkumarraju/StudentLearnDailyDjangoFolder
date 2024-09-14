from django.urls import path
from . import views

urlpatterns = [
    path('Student_Register/',views.register,name='Student_Register')
]
