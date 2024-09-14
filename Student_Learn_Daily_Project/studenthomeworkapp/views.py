from django.shortcuts import render

# Create your views here.
def studenthomework(request):
    return render(request,'studenthomework.html')