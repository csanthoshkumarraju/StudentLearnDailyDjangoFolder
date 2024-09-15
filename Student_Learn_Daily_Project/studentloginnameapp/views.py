# views.py
from django.shortcuts import render
from studentregisterapp.models import StudentRegistrationModel

def studentnavname(request):
    student_name = None

    student_id = request.session.get('student_id')
    if student_id:
        try:
            student = StudentRegistrationModel.objects.get(id=student_id)
            student_name = f"{student.first_name} {student.last_name}"
        except StudentRegistrationModel.DoesNotExist:
            student_name = "Guest"

    return render(request, 'studentloginnav.html', {'student_name': student_name})
