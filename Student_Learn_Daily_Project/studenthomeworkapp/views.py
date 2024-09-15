from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StudentHomeworkForm
from .models import StudentHomeworkModel
from django.utils import timezone
from datetime import datetime

def studenthomework(request, student_id):
    today = timezone.now().date()  # Get today's date

    if request.method == 'POST':
        # Handle search by date
        if 'search_date' in request.POST:
            search_date = request.POST.get('search_date')
            try:
                search_date = datetime.strptime(search_date, '%Y-%m-%d').date()
            except ValueError:
                messages.error(request, 'Invalid date format')
                search_date = today

            completed_homework = StudentHomeworkModel.objects.filter(completion_date=search_date)
            return render(request, 'studenthomework.html', {
                'form': StudentHomeworkForm(),
                'student_id': student_id,
                'today': today,
                'homework_today': StudentHomeworkModel.objects.filter(date=today),
                'homework_in_progress': StudentHomeworkModel.objects.filter(status='In Progress'),
                'completed_homework': completed_homework,
                'completed_homework_all': StudentHomeworkModel.objects.filter(status='Completed'),
                'search_date': search_date
            })

        # Handle marking homework as in progress
        elif 'mark_in_progress' in request.POST:
            hw_id = request.POST.get('hw_id')
            homework = get_object_or_404(StudentHomeworkModel, id=hw_id)
            homework.status = 'In Progress'
            homework.save()
            messages.success(request, 'Homework marked as In Progress.')
            return redirect('studenthomework', student_id=student_id)

        # Handle marking homework as completed
        elif 'mark_completed' in request.POST:
            hw_id = request.POST.get('hw_id')
            homework = get_object_or_404(StudentHomeworkModel, id=hw_id)
            homework.status = 'Completed'
            homework.completion_date = timezone.now().date()  # Set the completion date
            homework.save()
            messages.success(request, 'Homework marked as Completed.')
            return redirect('studenthomework', student_id=student_id)

        # Handle adding new homework
        else:
            form = StudentHomeworkForm(request.POST)
            if form.is_valid():
                homework = form.save(commit=False)
                homework.student_id = student_id
                homework.save()
                messages.success(request, "Homework added successfully. See it in the To-Do table.")
                return redirect('studenthomework', student_id=student_id)
            else:
                messages.error(request, 'Input fields are not valid')

    else:
        form = StudentHomeworkForm()

    return render(request, 'studenthomework.html', {
        'form': form,
        'student_id': student_id,
        'today': today,
        'homework_today': StudentHomeworkModel.objects.filter(date=today),
        'homework_in_progress': StudentHomeworkModel.objects.filter(status='In Progress'),
        'completed_homework': [],
        'completed_homework_all': StudentHomeworkModel.objects.filter(status='Completed'),
        'search_date': today
    })
