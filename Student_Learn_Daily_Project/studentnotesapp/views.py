from django.shortcuts import render,get_object_or_404,redirect
from studentregisterapp.models import StudentRegistrationModel
from .models import studentnotesmodel
from .forms import studentnotesform
from django.contrib import messages

# Create your views here.
# studentnotespage -- URl redirect

def studentnotespage(request,student_id):
    student = get_object_or_404(StudentRegistrationModel,id=student_id)
    student_name = f"{student.first_name} {student.last_name}"
    form = studentnotesform(request.POST or None)
    notes = studentnotesmodel.objects.filter(student=student)

    if request.method == 'POST':
        if 'addnotes' in request.POST:
            notes  = form.save(commit=False)
            notes.student = student
            notes.save()
            messages.success(request,'Notes added successfully')
            return redirect('studentnotespage',student_id=student_id)
        
        if 'delete_btn' in request.POST:
            notes_id = request.POST.get('notes_id')
            if notes_id:
                notes = get_object_or_404(studentnotesmodel,student=student,id=notes_id)
                notes.delete()
                messages.success(request,'Notes deleted successfully')
                return redirect('studentnotespage',student_id=student_id)
    return render(request,'studentnotes.html',
                  {
                    'student_id':student_id,
                    'student_name':student_name,
                    'form':form,
                    'notes':notes
                  })