# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from .forms import StudentHomeworkForm
# from .models import StudentHomeworkModel
# from studentregisterapp.models import StudentRegistrationModel
# from django.utils import timezone
# from datetime import datetime, timedelta

# def studenthomework(request, student_id):
#     student = get_object_or_404(StudentRegistrationModel, id=student_id)
#     student_name = f"{student.first_name} {student.last_name}"

#     form = StudentHomeworkForm()
#     add_homework_message = ""
#     mark_in_progress_message = ""
#     mark_completed_message = ""

#     if request.method == 'POST':
#         homework_id = request.POST.get('homework_id')
#         if 'add_homework' in request.POST:
#             form = StudentHomeworkForm(request.POST)
#             if form.is_valid():
#                 homework = form.save(commit=False)
#                 homework.student = student
#                 homework.save()
#                 add_homework_message = 'Homework added successfully.'
#                 return redirect('studenthomework', student_id=student_id)
        
#         elif 'mark_in_progress' in request.POST:
#             homework = get_object_or_404(StudentHomeworkModel, id=homework_id, student=student)
#             homework.status = 'In Progress'
#             homework.save()
#             mark_in_progress_message = 'Homework status updated to In Progress.'
#             return redirect('studenthomework', student_id=student_id)

#         elif 'mark_completed' in request.POST:
#             homework = get_object_or_404(StudentHomeworkModel, id=homework_id, student=student)
#             homework.status = 'Completed'
#             homework.save()
#             mark_completed_message = 'Homework status updated to Completed.'
#             return redirect('studenthomework', student_id=student_id)

#     todos = StudentHomeworkModel.objects.filter(student=student, status='To do').order_by('-date')
#     in_progress = StudentHomeworkModel.objects.filter(student=student, status='In Progress').order_by('-date')

#     search_date_str = request.GET.get('homework-date', timezone.now().date())
#     if isinstance(search_date_str, str):
#         try:
#             search_date = datetime.strptime(search_date_str, '%Y-%m-%d').date()
#         except ValueError:
#             search_date = timezone.now().date()
#     else:
#         search_date = search_date_str

#     start_of_day = datetime.combine(search_date, datetime.min.time())
#     end_of_day = start_of_day + timedelta(days=1)

#     completed_homework = StudentHomeworkModel.objects.filter(
#         student=student,
#         status='Completed',
#         date__gte=start_of_day.date(),
#         date__lt=end_of_day.date()
#     ).order_by('-date')

#     all_completed_homework = StudentHomeworkModel.objects.filter(
#         student=student,
#         status='Completed'
#     ).order_by('-date')

#     return render(request, 'studenthomework.html', {
#         'form': form,
#         'student_id': student_id,
#         'student_name': student_name,
#         'todos': todos,
#         'in_progress': in_progress,
#         'add_homework_message': add_homework_message,
#         'mark_in_progress_message': mark_in_progress_message,
#         'mark_completed_message': mark_completed_message,
#         'completed_homework': completed_homework,
#         'search_date': search_date,
#         'all_completed_homework': all_completed_homework,
#     })


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StudentHomeworkForm
from .models import StudentHomeworkModel
from studentregisterapp.models import StudentRegistrationModel
from django.utils import timezone
from datetime import datetime, timedelta

def studenthomework(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"

    form = StudentHomeworkForm()

    if request.method == 'POST':
        homework_id = request.POST.get('homework_id')
        if 'add_homework' in request.POST:
            form = StudentHomeworkForm(request.POST)
            if form.is_valid():
                homework = form.save(commit=False)
                homework.student = student
                homework.save()
                messages.success(request, 'Homework added successfully.')
                return redirect('studenthomework', student_id=student_id)
        
        elif 'mark_in_progress' in request.POST:
            homework = get_object_or_404(StudentHomeworkModel, id=homework_id, student=student)
            homework.status = 'In Progress'
            homework.date = timezone.now().date()
            homework.save()
            messages.success(request, 'Homework status updated to In Progress.')
            return redirect('studenthomework', student_id=student_id)

        elif 'mark_completed' in request.POST:
            homework = get_object_or_404(StudentHomeworkModel, id=homework_id, student=student)
            homework.status = 'Completed'
            homework.date = timezone.now().date()
            homework.save()
            messages.success(request, 'Homework status updated to Completed.')
            return redirect('studenthomework', student_id=student_id)

    todos = StudentHomeworkModel.objects.filter(student=student, status='To do').order_by('-date')
    in_progress = StudentHomeworkModel.objects.filter(student=student, status='In Progress').order_by('-date')

    search_date_str = request.GET.get('homework-date', timezone.now().date())
    if isinstance(search_date_str, str):
        try:
            search_date = datetime.strptime(search_date_str, '%Y-%m-%d').date()
        except ValueError:
            search_date = timezone.now().date()
    else:
        search_date = search_date_str

    start_of_day = datetime.combine(search_date, datetime.min.time())
    end_of_day = start_of_day + timedelta(days=1)

    completed_homework = StudentHomeworkModel.objects.filter(
        student=student,
        status='Completed',
        date__gte=start_of_day.date(),
        date__lt=end_of_day.date()
    ).order_by('-date')

    all_completed_homework = StudentHomeworkModel.objects.filter(
        student=student,
        status='Completed'
    ).order_by('-date')

    return render(request, 'studenthomework.html', {
        'form': form,
        'student_id': student_id,
        'student_name': student_name,
        'todos': todos,
        'in_progress': in_progress,
        'completed_homework': completed_homework,
        'search_date': search_date,
        'all_completed_homework': all_completed_homework,
    })
