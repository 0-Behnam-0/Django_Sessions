'''
# First Code 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return HttpResponse("""<h1>Hello, Django</h1>
     This is blog page""")
'''

# Second Code 
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request,'blogpage/blog.html',context={"Name":'Behnam',
        "Age":20})