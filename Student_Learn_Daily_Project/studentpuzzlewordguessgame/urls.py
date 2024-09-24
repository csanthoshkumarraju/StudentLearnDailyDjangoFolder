from django.urls import path
from . import views

urlpatterns = [
    path('studentwordpuzleguessgame/<int:student_id>/',views.studentwordpuzleguessgame,name='studentwordpuzleguessgame')
]
