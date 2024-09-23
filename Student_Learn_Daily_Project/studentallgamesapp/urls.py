from django.urls import path
from . import views

urlpatterns = [
    path('studentallgames/<int:student_id>/',views.studentallgames,name="studentallgames")
]
