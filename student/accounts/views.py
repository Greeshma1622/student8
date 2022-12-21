from django.shortcuts import render,redirect
from .models import Contact,Staff,Departments
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')


def department(request):
    dict_dept={
        'department':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
        return render(request,'contact.html',dicts)
    return render(request,'contact.html')

def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('newhome')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username and password')
            return redirect('signin')
    return render(request,'signin.html')


def signup(request):
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            phno = request.POST['phno']
            password2 = request.POST['password2']
            if password == password2 :
                if Staff.objects.filter(email = email).exists():
                    messages.info(request,'email taken')
                    return redirect('signup')
                else:
                    customer = Staff.objects.create(email = email,name = name,password = password,phno = phno)
                    customer.save()
                    messages.info(request,'user created')
                    return redirect('signin')
            else:
                messages.info(request,'password is not match')
                return redirect('signup')
        else:
            return render(request,'signup.html')
   

def forgot(request):
    if request.method == "POST":
        email= request.POST['email']
        password = request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('signin')
        else:
            messages.error(request,'invalid data')
            return redirect('forgot')
    return render(request,'forgot.html')