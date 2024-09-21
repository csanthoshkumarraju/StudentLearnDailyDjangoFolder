from django.urls import path
from . import views

urlpatterns = [
    path('studentmonthlypage/<int:student_id>/',views.studentmonthlypage,name="studentmonthlypage")
]
