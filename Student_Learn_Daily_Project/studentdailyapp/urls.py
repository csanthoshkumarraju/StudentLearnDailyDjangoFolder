from django.urls import path
from . import views

urlpatterns = [
       path('studentdailypage/<int:student_id>',views.studentdailypage,name='studentdailypage')
]
