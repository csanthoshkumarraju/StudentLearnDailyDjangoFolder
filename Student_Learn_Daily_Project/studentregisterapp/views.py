# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import StudentRegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             messages.success(request, "Registration successful")
#             request.session['registration_email'] = student.email
#             return redirect('student_register_otp')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = StudentRegistrationForm()

#     return render(request, 'studentlearndailyregister.html', {'form': form})


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import StudentRegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             messages.success(request, "Registration successful")
#             return redirect('studentlogin')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = StudentRegistrationForm()

#     return render(request, 'studentlearndailyregister.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentRegistrationForm
from studentregisterapp.models import StudentRegistrationModel

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create student instance but do not save it yet
            student = StudentRegistrationModel(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            student.set_password(password)  # Hash the password
            student.save()
            messages.success(request, "Registration successful")
            return redirect('studentlogin')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentRegistrationForm()

    return render(request, 'studentlearndailyregister.html', {'form': form})
