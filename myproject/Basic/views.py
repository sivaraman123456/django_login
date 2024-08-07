from django.shortcuts import render,redirect
from .form import CreateUserForm,SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Signup
def home(request):
    return render(request,'home.html')



def register(request):
    if request.method == 'POST':
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=name).exists():
                messages.warning(request, "Username already exists")
                return redirect("Register")
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email already exists")
                return redirect("Register")
            else:
                user = User.objects.create_user(username=name, email=email, password=password1)
                user.save()
                messages.success(request, "Your account has been created")
                return redirect("Login")
        else:
            messages.warning(request,"password Mismatching....!")
            return redirect("Register")
    else:
        form =CreateUserForm()
        return render(request,'register.html',{'form':form})
    

def signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        print("form:",form)
        if form.is_valid():
            form.save()
            return redirect("Home")
    
    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form})
    
def dashboard(request):
    return render(request,'dashboard.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
       
        try:
            user = Signup.objects.get(email=email)
            print("users_name:",user.name,"email:",user.email)
            
            if user is not None:
                return redirect('Dashboard')  # Redirect to a dashboard or another view after successful login
            else:
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        except Signup.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')

    
