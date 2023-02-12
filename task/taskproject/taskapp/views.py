from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Data
from .forms import Data_form
import sweetify

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'main.html')
        else:
            messages.info(request, 'invalid username/password')
            return render(request,'login.html')

    return render(request, 'login.html',)

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name','')
        last_name = request.POST.get('last_name')
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'user/email already exist')
                return render(request,'register.html')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password)
                user.save();
                print('user created successfully')
                return render(request,'login.html',dict(user=user))
        return render(request,'main.html')
    return render(request,'register.html',)


def logout(request):
    auth.logout(request)
    return render(request,'home.html')
def dataview(request):

    data= Data.objects.all()
    form1=Data_form(request.POST or None)

    if request.method == "POST":
        name=request.POST['name']
        date_of_birth=request.POST['date_of_birth']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        mail=request.POST['mail']
        address=request.POST['address']
        department=request.POST['department']
        purposes=request.POST['purposes']
        form=Data(name=name,date_of_birth=date_of_birth,age=age,gender=gender,phone=phone,mail=mail,
                  address=address,department=department,purposes=purposes)
        form.save()
        print('successfully updated')
    return render(request,'details.html',dict(data=data,form=form1))

