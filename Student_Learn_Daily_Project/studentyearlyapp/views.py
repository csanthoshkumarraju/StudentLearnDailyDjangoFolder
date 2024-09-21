from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentyearlyplan
from .forms import studentyealyform
import datetime
from django.contrib import messages
# Create your views here.




def studentyearlypage(request,student_id):
    student = get_object_or_404(StudentRegistrationModel,id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    form = studentyealyform(request.POST or None)
    now = datetime.datetime.now()
    curr_year = now.year
    yearly_plans_todos = studentyearlyplan.objects.filter(student=student,yealy_plan_status="To Do")
    yealy_plans_inp = studentyearlyplan.objects.filter(student=student,yealy_plan_status="In Progress")
    yearly_plans_completed = studentyearlyplan.objects.filter(student=student,yealy_plan_status="Completed")


    if request.method == 'POST':
        if 'addyearlyplan' in request.POST:
            if form.is_valid():
               yearly_plan = form.save(commit=False)
               yearly_plan.student = student
               yearly_plan.save()
               messages.success(request,'Yearly plan added successfully!')
               return redirect('studentyearlypage',student_id=student_id) 
            else:
               messages.error(request,'Form is not valid')

        if 'yearlyplaninp' in request.POST:
            yearly_plan_id = request.POST.get('yearly_id')
            if yearly_plan_id:
                yearly_plan = get_object_or_404(studentyearlyplan,student=student,id=yearly_plan_id)
                yearly_plan.yealy_plan_status = 'In Progress'
                yearly_plan.save()
                messages.success(request,'yearly plan status updated to In Progress')
                return redirect('studentyearlypage',student_id=student_id)
            else:
               messages.error(request,'Form is not valid') 

        if 'yearlyplancomp' in request.POST:
            yearly_plan_id = request.POST.get('yearly_id')
            if yearly_plan_id:
                yearly_plan = get_object_or_404(studentyearlyplan,student=student,id=yearly_plan_id)
                yearly_plan.yealy_plan_status = 'Completed'
                yearly_plan.save()
                messages.success(request,'Yearly plan status updated to Completed')
                return redirect('studentyearlypage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid') 



    else:
        form = studentyealyform()


    return render(request,'studentyearly.html',{
        'student_name':student_name,
        'student_id':student_id,
        'curr_year':curr_year,
        'form':form,
        'yearly_plans_todos':yearly_plans_todos,
        'yealy_plans_inp':yealy_plans_inp,
        'yearly_plans_completed':yearly_plans_completed
    })
