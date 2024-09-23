from django.urls import path
from . import views

urlpatterns = [
    path('studentheadortails/<int:student_id>/',views.studentheadortails,name='studentheadortails')
]
