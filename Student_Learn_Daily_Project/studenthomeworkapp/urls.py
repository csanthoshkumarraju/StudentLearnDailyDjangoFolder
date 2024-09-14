from django.urls import path
from . import views

urlpatterns = [
    path('studenthomework/',views.studenthomework,name='studenthomework')
]
