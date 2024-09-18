from django.urls import path
from . import views


urlpatterns = [
    path('studentasignments/<int:student_id>/',views.studentasignments,name='studentasignments')
]
