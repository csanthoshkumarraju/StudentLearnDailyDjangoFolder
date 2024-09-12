from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Student_Introduction_Page(request):
    return render(request,'student_web_app_introduction.html')
