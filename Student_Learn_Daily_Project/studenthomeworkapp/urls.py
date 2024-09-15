from django.urls import path
from . import views

urlpatterns = [
    path('studenthomework/<int:student_id>/', views.studenthomework, name='studenthomework'),
]
