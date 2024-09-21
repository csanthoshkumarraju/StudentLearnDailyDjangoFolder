from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .forms import studentmonthlyform
from .models import studentmonthlyplanmodel
from django.contrib import messages
import datetime


def studentmonthlypage(request,student_id):
    student = get_object_or_404(StudentRegistrationModel,id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    form = studentmonthlyform(request.POST or None)
    now = datetime.datetime.now()
    curr_month = now.strftime("%B")
    curr_year = now.year
    monthly_plan_todos = studentmonthlyplanmodel.objects.filter(student=student,monthly_status="To Do")
    monthly_plan_inp = studentmonthlyplanmodel.objects.filter(student=student,monthly_status="In Progress")
    monthly_plan_completed = studentmonthlyplanmodel.objects.filter(student=student,monthly_status="Completed")

    if request.method == 'POST':
        if 'addmonthlyplan' in request.POST:
            if form.is_valid():
                monthly_plan = form.save(commit=False)
                monthly_plan.student = student
                monthly_plan.save()
                messages.success(request,'The monthly plan has been added successfully.')
                return redirect('studentmonthlypage',student_id=student_id)
            else:
                messages.error('Form is not valid')

        if 'monthly_in_progress_btn' in request.POST:
            monthly_id = request.POST.get('monthly_id')
            if monthly_id:
                monthly_plan = get_object_or_404(studentmonthlyplanmodel,id=monthly_id,student=student)
                monthly_plan.monthly_status = "In Progress"
                monthly_plan.save()
                messages.success(request,'Monthly plan status updated to In Progress')
                return redirect('studentmonthlypage',student_id=student_id)
            else:
                messages.error('Monthly Plan is not available')

        if 'monthly_plan_completed' in request.POST:
            monthly_id = request.POST.get('monthly_id')
            if monthly_id:
                monthly_plan = get_object_or_404(studentmonthlyplanmodel,id=monthly_id,student=student)
                monthly_plan.monthly_status = "Completed"
                monthly_plan.save()
                messages.success(request,'Monthly plan status updated to Completed')
                return redirect('studentmonthlypage',student_id=student_id)
            
            else:
                messages.error('Monthly Plan is not available')


    
    else:
        form = studentmonthlyform()
    form = studentmonthlyform(request.POST)
    form = studentmonthlyform(request.POST)
    return render(request,'studentmonthly.html',{'student_name':student_name,
                                                 'student_id':student_id,
                                                 'form':form,'curr_month':curr_month,
                                                 'curr_year':curr_year,
                                                 'monthly_plan_todos':monthly_plan_todos,
                                                 'monthly_plan_inp':monthly_plan_inp,
                                                 'monthly_plan_completed':monthly_plan_completed})
