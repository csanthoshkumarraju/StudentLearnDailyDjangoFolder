from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentgoalsmodel
from .forms import studentgoalform
from django.contrib import messages

# Create your views here.


def studentgoalspage(request,student_id):
    student = get_object_or_404(StudentRegistrationModel,id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    added_goals = studentgoalsmodel.objects.filter(student=student,goal_status="To Do")
    completed_goals = studentgoalsmodel.objects.filter(student=student,goal_status="Completed")
    form = studentgoalform(request.POST or None)

    if request.method == 'POST':
        if 'addgoal' in request.POST:
            if form.is_valid():
                goal = form.save(commit=False)
                goal.student = student
                goal.save()
                messages.success(request,'Goal added successfully')
                return redirect('studentgoalspage',student_id=student_id)
            

        if 'completed_goal_btn' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal = get_object_or_404(studentgoalsmodel,student=student,id=goal_id)
                goal.goal_status="Completed"
                goal.save()
                messages.success(request,'Goal status updated to completed')
                return redirect('studentgoalspage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid')
            
        if 'todo_goal_btn' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal = get_object_or_404(studentgoalsmodel,student=student,id=goal_id)
                goal.goal_status="To Do"
                goal.save()
                messages.success(request,'Goal status updated to To Do')
                return redirect('studentgoalspage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid')

        if 'delete_add_btn' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal = get_object_or_404(studentgoalsmodel,student=student,id=goal_id)
                goal.delete()
                messages.success(request,'Goal deleted successfully')
                return redirect('studentgoalspage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid')

        if 'delete_comp_btn' in request.POST:
            goal_id = request.POST.get('goal_id')
            if goal_id:
                goal = get_object_or_404(studentgoalsmodel,student=student,id=goal_id)
                goal.delete()
                messages.success(request,'Goal deleted successfully')
                return redirect('studentgoalspage',student_id=student_id)
            else:
                messages.error(request,'Form is not valid')

    return render(request,'studentgoals.html',
                  {
                    'student_id':student_id,
                    'student_name':student_name,
                    'form':form,
                    'added_goals':added_goals,
                    'completed_goals':completed_goals
                  }
                  
                  )