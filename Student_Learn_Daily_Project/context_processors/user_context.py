from studentregisterapp.models import StudentRegistrationModel

def student_context(request):
    student_name = ""
    student_id = request.session.get('student_id')
    
    if student_id:
        try:
            student = StudentRegistrationModel.objects.get(pk=student_id)
            student_name = f"{student.first_name} {student.last_name}"
        except StudentRegistrationModel.DoesNotExist:
            student_name = ""
    
    return {
        'student_name': student_name
    }


