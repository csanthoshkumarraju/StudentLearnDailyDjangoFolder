from django.urls import path
from . import views

urlpatterns = [
    path('studentgoalspage/<int:student_id>/',views.studentgoalspage,name="studentgoalspage")
]
