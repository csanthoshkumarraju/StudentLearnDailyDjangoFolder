from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentcollabaratemodel
from .forms import studentvollabarateforms
from django.contrib import messages
# Create your views here.
# studentcollabarate

# def studentcollabarate(request,student_id):
#     student = get_object_or_404(StudentRegistrationModel,id=student_id)
#     student_name = f"{student.first_name} {student.last_name}"
#     form  = studentvollabarateforms(request.POST or None)

#     if request.method == 'POST':
#         if 'sendmessage' in request.POST:
#             if form.is_valid():
#                 message = form.save(commit=False)
#                 message.student = student
#                 message.save()
#                 messages.success(request,'Sent a message')
#                 return redirect('studentcollabarate',student_id=student_id)


#     return render(request,'studentcollobarate.html',{
#         'student_id':student_id,
#         'student_name':student_name,
#         'form':form
#     })

def studentcollabarate(request, student_id):
    student = get_object_or_404(StudentRegistrationModel, id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    form = studentvollabarateforms(request.POST or None)
    messages_list = studentcollabaratemodel.objects.all().order_by('date')

    if request.method == 'POST':
        if 'sendmessage' in request.POST:
            if form.is_valid():
                message = form.save(commit=False)
                message.student = student
                message.save()
                messages.success(request, 'Sent a message')
                return redirect('studentcollabarate', student_id=student_id)

        if 'delete_message' in request.POST:
            message_id = request.POST.get('message_id')
            message = get_object_or_404(studentcollabaratemodel, id=message_id)

            if message.student == student:
                message.delete()
                messages.success(request, 'Message deleted successfully.')
                return redirect('studentcollabarate', student_id=student_id)
        if 'edit_message' in request.POST:
            message_id = request.POST.get('message_id')
            message = get_object_or_404(studentcollabaratemodel, id=message_id)

            if message.student == student:
                message.message = request.POST.get('edited_message')
                message.save()
                messages.success(request, 'Message updated successfully.')
                return redirect('studentcollabarate', student_id=student_id)
            
    return render(request, 'studentcollobarate.html', {
        'student_id': student_id,
        'form': form,
        'messages_list': messages_list,
        'current_user': student,
        'student_name': student_name
    })

