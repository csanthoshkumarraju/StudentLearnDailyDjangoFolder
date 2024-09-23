from django.urls import path
from . import views

urlpatterns = [
    path('studentnumberguessing/<int:student_id>/',views.studentnumberguessing,name='studentnumberguessing')
]
