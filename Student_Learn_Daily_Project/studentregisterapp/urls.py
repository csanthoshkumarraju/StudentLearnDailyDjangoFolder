from django.urls import path
from . import views

urlpatterns = [
    path('/Student_Register',views.Student_Register,name='Student_Register')
]
