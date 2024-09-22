from django.urls import path
from . import views

urlpatterns = [
    path('studentnotespage/<int:student_id>/',views.studentnotespage,name="studentnotespage")
]
