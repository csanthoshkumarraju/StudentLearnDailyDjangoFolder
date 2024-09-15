from django.shortcuts import render, redirect
from studentregisterapp.models import StudentRegistrationModel
from django.http import HttpResponse
from .forms import LoginForm

def studentlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                student = StudentRegistrationModel.objects.get(email=email)
                if student.password == password:
                    request.session['student_id'] = student.id
                    return redirect('studenthomework', student_id=student.id)
                else:
                    form.add_error(None, 'Incorrect password')
            except StudentRegistrationModel.DoesNotExist:
                form.add_error(None, 'Email not registered')
    else:
        form = LoginForm()

    return render(request, 'studentlogin.html', {'form': form})
