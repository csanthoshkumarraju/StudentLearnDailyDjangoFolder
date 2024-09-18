from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentassignmentsmodel
from .forms import studentassignmentsform 
from django.contrib import messages
# Create your views here.
# studentassignments.html

# def studentasignments(request,student_id):
#     student = get_object_or_404(StudentRegistrationModel,id=student_id)
#     student_name = f"{student.first_name} {student.last_name}"
#     assignments = student.assignments.all()
#     form = studentassignmentsform(request.POST)

#     if request.method == 'POST':
#         assignment_id = request.POST.get('assignment_id')
#         if 'add_assignment' in request.POST:
#             if form.is_valid():
#                 assignment = form.save(commit=False)
#                 assignment.student = student
#                 assignment.save()
#                 messages.success(request,'Assignment added successfully.')
#                 return redirect('studentasignments',student_id=student_id)
    
#         if 'mark_in_progress' in request.POST:
#             assignment_id = request.POST.get('assignment_id')  # Get the assignment ID from the POST data
#             assignment = get_object_or_404(studentassignmentsmodel, id=assignment_id, student=student)
#             assignment.status = 'In Progress'
#             assignment.save()
#             messages.success(request, 'Assignment status updated to In Progress.')
#             return redirect('studentasignments', student_id=student_id)
#     assignments_todos = studentassignmentsmodel.objects.filter(student=student,status='To Do')

#     return render(request,'studentassignments.html',{'student_name':student_name,'student_id':student_id,'form': form,'assignments_todos':assignments_todos,'assignments': assignments})


def studentasignments(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    assignments = student.assignments.all()
    form = studentassignmentsform(request.POST or None)

    if request.method == 'POST':
        if 'add_assignment' in request.POST:
            if form.is_valid():
                assignment = form.save(commit=False)
                assignment.student = student
                assignment.save()
                messages.success(request, 'Assignment added successfully.')
                return redirect('studentasignments', student_id=student_id)

        if 'mark_in_progress' in request.POST:
            assignment_id = request.POST.get('assignment_id')
            if assignment_id:  
                assignment = get_object_or_404(studentassignmentsmodel, id=assignment_id, student=student)
                assignment.status = 'In Progress'
                assignment.save()
                messages.success(request, 'Assignment status updated to In Progress.')
                return redirect('studentasignments', student_id=student_id)

        if 'mark_as_completed' in request.POST:
            assignment_id = request.POST.get('assignment_id')
            if assignment_id: 
                assignment = get_object_or_404(studentassignmentsmodel, id=assignment_id, student=student)
                assignment.status = "Completed"
                assignment.save()
                messages.success(request, 'Assignment status updated to Completed.')
                return redirect('studentasignments', student_id=student_id)

    assignments_todos = studentassignmentsmodel.objects.filter(student=student, status='To Do')
    assignment_in_progress = studentassignmentsmodel.objects.filter(student=student, status='In Progress')
    assignments_completed = studentassignmentsmodel.objects.filter(student=student, status='Completed')

    return render(request, 'studentassignments.html', {
        'student_name': student_name,
        'student_id': student_id,
        'form': form,
        'assignments_todos': assignments_todos,
        'assignments': assignments,
        'assignment_in_progress': assignment_in_progress,
        'assignments_completed': assignments_completed
    })


