# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm

# def studentlogin(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('studenthomework')
#             else:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = LoginForm()

#     return render(request, 'studentlogin.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm
from django.contrib import messages
from studentregisterapp.models import StudentRegistrationModel

def studentlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # Log the user in
                auth_login(request, user)

                # Redirect to studenthomework page
                messages.success(request, 'Login Successful')
                return redirect('studenthomework', student_id=user.id)
                
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'studentlogin.html', {'form': form})

