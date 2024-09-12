from django.urls import path
from . import views

urlpatterns = [
    path('', views.Student_Introduction_Page, name='Student_Introduction_Page'),
]