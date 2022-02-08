from django import http
from django.contrib.auth import authenticate, login
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from apps import models
from .form import StudentsForm
from .models import Employees, Students

# Create your views here.

def StudentRegister(request):
    if request.method =='POST':
        fna = request.POST['sfname']
        lna = request.POST['slname']
        ag = request.POST['sage']
        ad = request.POST['saddress']
        con = request.POST['scontacts']
        em = request.POST['semail']
        us = request.POST['username']
        pas = request.POST['password']
        reg = Students.objects.create(First_Name=fna,Last_Name=lna,Age=ag,Address=ad,Contacts=con,Email=em,username=us,password=pas)
        reg.save()
        return render (request,'login.html')
    else:
        return render (request,'studentpost.html')

def EmployeeRegister(request):
    if request.method =='POST':
        fna = request.POST['sfname']
        lna = request.POST['slname']
        ag = request.POST['sage']
        ad = request.POST['saddress']
        con = request.POST['scontacts']
        em = request.POST['semail']
        us = request.POST['username']
        pas = request.POST['password']
        reg = Employees.objects.create(First_Name=fna,Last_Name=lna,Age=ag,Address=ad,Contacts=con,Email=em,username=us,password=pas)
        reg.save()
        return redirect ('adminstudentview')
    else:
        return render (request,'employeepost.html')


def home(request) :
    return render (request,'home.html')


def login(request) :
    return render (request,'login.html')

def authentic(request) :
    if request.method == 'POST':
        usr = request.POST['username']
        pas = request.POST['password']

        user = authenticate(username=usr, password=pas)
        if user is not None :
            return redirect ('adminstudentview')

        try:
            s = Employees.objects.get(username=usr, password=pas)
            if s is not None :
                return redirect ('StudentsView')

        except:
            us = Students.objects.get(username=usr, password=pas)
            # return HttpResponse(us)
            if us is not None and us.status == "Yes" :
                # return HttpResponse(us.Age)
                return render(request,'individual.html',{'view':us})
            else :
                return HttpResponse("Youre Not Approved By Admin...Kindly wait for The Approval")

        # else :
        #     return HttpResponse("Youre  Not Autherised User")


def individualview(request) :
    return render(request,'individual.html')


def StudentsView(request) :
    student = Students.objects.all()
    return render (request,'studentview.html',{'view':student})

def StudentTeachersView(request) :
    employee = Employees.objects.all()
    return render (request,'student-teacherview.html',{'read': employee})

def adminstudentview(request) :
    student = Students.objects.all()
    employee = Employees.objects.all()
    return render (request,'admin-view.html',{'view':student,'read': employee})

def StudentApprove(request,id) :
    approvrid = Students.objects.get(id=id)
    approvrid.status = "Yes"
    approvrid.save()
    return redirect('adminstudentview')


def EmployeeDelete(request,id):
    delid =Employees.objects.get(id=id)
    delid.delete()
    return redirect('adminstudentview')

def EmployeeEdit(request,id):
    editid =Employees.objects.get(id=id)
    return render(request,'empupdate.html',{'edit':editid})


def EmployeeUpdate(request,id):

    studedit = Employees.objects.get(id=id)
    fna = request.POST['First_Name']
    lna = request.POST['Last_Name']
    ag = request.POST['Age']
    ad = request.POST['Address']
    con = request.POST['Contacts']
    em = request.POST['Email']

    studedit.First_Name = fna
    studedit.Last_Name = lna
    studedit.Age = ag
    studedit.Address = ad
    studedit.Contacts = con
    studedit.email = em

    studedit.save()
    return redirect('adminstudentview')



def StudentDelete(request,id):
    delid =Students.objects.get(id=id)
    delid.delete()
    return redirect('login')


def StudentEdit(request,id):
    editid =Students.objects.get(id=id)
    return render(request,'update.html',{'edit':editid})

def StudentUpdate(request,id):
    studedit = Students.objects.get(id=id)
    fna = request.POST['First_Name']
    lna = request.POST['Last_Name']
    ag = request.POST['Age']
    ad = request.POST['Address']
    con = request.POST['Contacts']
    em = request.POST['Email']
    # form = Students.objects.create(First_Name=fna,Last_Name=lna,Age=ag,Address=ad,Contacts=con,Email=em)
    studedit.First_Name = fna
    studedit.Last_Name = lna
    studedit.Age = ag
    studedit.Address = ad
    studedit.Contacts = con
    studedit.email = em

    # if studedit.is_valid():
    studedit.save()
    return redirect('login')

    # if form.is_valid():
    #     form.save()
    
    # return render(request,'update.html',{'edit':studedit})


def index(request) :
    return redirect(request,'index.html')