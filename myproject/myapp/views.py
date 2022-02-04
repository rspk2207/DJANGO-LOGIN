from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import student
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        roll = request.POST['roll']
        college = request.POST['clg']
        year = request.POST['year']
        gender = request.POST.get('gender','')
        password = request.POST['password1']
        verify = request.POST['password2']
        if (username=='' or name=='' or email=='' or roll=='' or college=='' or year=='' or gender=='' or password=='' or verify==''): 
            messages.error(request,"ALL FIELDS ARE MANDATORY")
            return redirect('/')
        else:
            if User.objects.filter(username = username):
                messages.error(request,"USERNAME ALREADY EXISTS")
                return redirect('/')
            elif User.objects.filter(email = email):
                messages.error(request,"EMAIL ALREADY EXISTS")
                return redirect('/')
            else:
                if password == verify:    
                    user = User.objects.create_user(username = username,email = email,password = password)
                    user.student.name = name
                    user.student.roll_number = roll
                    user.student.college = college
                    user.student.year = year
                    user.student.gender = gender
                    user.save()
                    return redirect('login')
                else:
                    messages.error(request,"PASSWORD DOES NOT MATCH")
                    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,'INVALID CREDENTIALS')
            return redirect('login')
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')
    else:
        messages.error(request,"LOGIN ONCE AGAIN")
        return redirect('login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('login')
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        messages.error(request,"LOGIN ONCE AGAIN")
        return redirect('login')