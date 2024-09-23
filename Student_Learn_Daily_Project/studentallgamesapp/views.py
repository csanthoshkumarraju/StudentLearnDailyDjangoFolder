from django.shortcuts import render,get_object_or_404
from studentregisterapp.models import StudentRegistrationModel
# Create your views here.


def studentallgames(request,student_id):
    student = get_object_or_404(StudentRegistrationModel,id=student_id)
    student_name = f"{student.first_name} {student.last_name}"

    return render(request,'studentallgames.html',{
        'student_id':student_id,
        'student_name':student_name
    })
      