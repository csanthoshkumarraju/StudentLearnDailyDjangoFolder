from django.urls import path
from . import views

urlpatterns = [
    path('studentcollabarate/<int:student_id>/',views.studentcollabarate,name='studentcollabarate')
]

