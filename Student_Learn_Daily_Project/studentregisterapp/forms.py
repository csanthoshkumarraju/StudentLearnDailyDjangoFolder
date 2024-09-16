# from django import forms
# from .models import StudentRegistrationModel

# class StudentRegistrationForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'registration-confirm-password-input'}), label='Confirm Password')

#     class Meta:
#         model = StudentRegistrationModel
#         fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'registration-fname', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'registration-lname', 'placeholder': 'Last Name'}),
#             'email': forms.EmailInput(attrs={'class': 'registration-email-input', 'placeholder': 'Email Id'}),
#             'password': forms.PasswordInput(attrs={'class': 'registration-password-input', 'placeholder': 'Password'}),
#             'confirm_password': forms.PasswordInput(attrs={'class': 'registration-confirm-password-input', 'placeholder': 'Confirm Password'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password and confirm_password and password != confirm_password:
#             self.add_error('confirm_password', "Passwords do not match")


from django import forms
from .models import StudentRegistrationModel

class StudentRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'registration-confirm-password-input'}), label='Confirm Password')

    class Meta:
        model = StudentRegistrationModel
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'registration-fname', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'registration-lname', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'registration-email-input', 'placeholder': 'Email Id'}),
            'password': forms.PasswordInput(attrs={'class': 'registration-password-input', 'placeholder': 'Password'}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'registration-confirm-password-input', 'placeholder': 'Confirm Password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

