# from django import forms

# class LoginForm(forms.Form):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'placeholder': 'Enter your registered email address',
#             'class': 'student-login-email'
#         })
#     )
#     password = forms.CharField(
#         required=True,
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Enter your password',
#             'class': 'student-login-password'
#         })
#     )


from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your registered email address',
            'class': 'student-login-email'
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'student-login-password'
        })
    )
