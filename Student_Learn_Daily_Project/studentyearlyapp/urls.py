from django.urls import path
from . import views

urlpatterns = [
    path('studentyearlypage/<int:student_id>/',views.studentyearlypage,name="studentyearlypage")
]
