from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResetPasswordForm
from studentregisterapp.models import StudentRegistrationModel

def student_reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'studentresetpasswordapp.html', {'form': form})

            try:
                student = StudentRegistrationModel.objects.get(email=email)
                student.set_password(password)  # Hash the new password
                student.save()
                messages.success(request, 'Password has been reset successfully. You can now log in.')
                return redirect('studentlogin')
            except StudentRegistrationModel.DoesNotExist:
                messages.error(request, 'Email address not found.')
                return render(request, 'studentresetpasswordapp.html', {'form': form})
    else:
        form = ResetPasswordForm()

    return render(request, 'studentresetpasswordapp.html', {'form': form})
