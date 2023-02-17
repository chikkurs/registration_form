from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Data,Department,Branch
from .forms import Data_form
from django.http import JsonResponse
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
            return render(request,'main.html',dict(user=user))
        else:
            messages.info(request, 'invalid username/password')
            return render(request,'login.html')

    return render(request, 'login.html')

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
                return render(request,'login.html')
        return render(request,'register.html')
    return render(request,'register.html',)


def logout(request):
    auth.logout(request)
    return render(request,'home.html')

def dataview(request):

    data= Data.objects.all()
    form1=Data_form(request.POST or None)
    
    if request.method == "POST":
        
        name=request.POST['name']
        dob=f"{request.POST['date_of_birth_year']}-{request.POST['date_of_birth_month']}-{request.POST['date_of_birth_day']}"
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phone']
        mail=request.POST['mail']
        address=request.POST['address']
        department_id=request.POST['department']
        department=Department.objects.get(pk=department_id)
        branch_name=request.POST['branch']
        branch=Branch.objects.filter(name=branch_name)
        print(branch)
        purposes=request.POST['purposes']
        form=Data(name=name,date_of_birth=dob,age=age,gender=gender,phone=phone,mail=mail,
                  address=address,department=department,purposes=purposes,branch=branch,department_id=department_id,branch_name=branch_name)
        form.save()
        print('successfully updated')
    return render(request,'details.html',dict(data=data,form=form1))
def load_branches(request):
    department_id = request.GET.get('id')
    department_id=int(department_id)
    branches=Branch.objects.filter(branch_id=department_id).all()
    data=[]
    for i in branches:
        data.append(i.name)
    return JsonResponse({"data":data}, safe=False)
