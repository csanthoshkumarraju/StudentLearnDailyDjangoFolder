from django.urls import path
from . import views

urlpatterns = [
    path('studentwordgame/<int:student_id>/',views.studentwordgame,name="studentwordgame")
]
