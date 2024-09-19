from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentdailymodel
from .forms import studentdailyplan
from django.contrib import messages
import datetime
# Create your views here.

def studentdailypage(request,student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    dailyplans = studentdailymodel.objects.all()
    form = studentdailyplan(request.POST or None)
    today_date = datetime.date.today()
    
    daily_plan_to_do = studentdailymodel.objects.filter(student=student,daily_status='To do')
    daily_plans_in_progress = studentdailymodel.objects.filter(student=student,daily_status = 'In Progress')
    daily_plans_completed = studentdailymodel.objects.filter(student = student,daily_status='Completed')

    if request.method == 'POST':
        if 'adddailyplan' in request.POST:
            if form.is_valid():
                daily_plan = form.save(commit=False)
                daily_plan.student = student
                daily_plan.save()
                messages.success(request,'Daily plan added successfully.')
                return redirect('studentdailypage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid')

        if 'daily_plan_in_progress' in request.POST:
            daily_plan_id = request.POST.get('daily_id')
            if daily_plan_id:
                daily_plan = get_object_or_404(studentdailymodel,id = daily_plan_id,student=student)
                daily_plan.daily_status = "In Progress"
                daily_plan.save()
                messages.success(request,'Daily plan status updated to In Progress')
                return redirect('studentdailypage',student_id=student_id)
            
        if 'daily_plan_complete' in request.POST:
            daily_plan_id = request.POST.get('daily_id')
            if daily_plan_id:
                daily_plan = get_object_or_404(studentdailymodel,id = daily_plan_id,student = student)
                daily_plan.daily_status = "Completed"
                daily_plan.save()
                messages.success(request,'Daily plan status updated to Completed')
                return redirect('studentdailypage',student_id=student_id)
    else:
        form = studentdailyplan()
    return render(request,'studentdaily.html',{'student_id':student_id,'student_name':student_name,'form':form,'today_date':today_date,'daily_plan_to_do':daily_plan_to_do,'daily_plans_in_progress':daily_plans_in_progress,'daily_plans_completed':daily_plans_completed})