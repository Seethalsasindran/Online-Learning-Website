from django.shortcuts import render,redirect
from .models import students,contact,newsletter,Subjects
from django.contrib import messages
#from django.http import HttpResponse

# Create your views here.
def myfunc(request):
    if request.method=="POST":
        email3=request.POST['Email']
        newsletter(email=email3).save()
    return render(request,'main.html')
def myfunc1(request):
    if request.method=="POST":
        email1=request.POST['email']
        name1=request.POST['name']
        password1=request.POST['password']
        emailexist=students.objects.filter(email=email1)
        if emailexist:
            messages.info(request,'Email already exist')
            return render(request,'register.html')
        else:
            students(email=email1,name=name1,password=password1).save()
            messages.info(request,'The user '+request.POST['name']+' regiistered successfully')
   
            
    return render(request,'register.html')
def myfunc2(request):
    if request.method=='POST':
        try:
            students_details=students.objects.get(email=request.POST['email'],password=request.POST['password'])
        
            request.session['email']=students_details.email
            return redirect('myfunc5')
        except students.DoesNotExist as e:
            messages.info(request,'E-Mail does not exist')


    return render(request,'login.html')
def myfunc3(request):
    return render(request,'about.html')
def myfunc4(request):
    if request.method=='POST':
        name2=request.POST['yourname']
        email2=request.POST['e-mail']
        phone2=request.POST['phonenumber']
        message2=request.POST['message']
        contact(name=name2,email=email2,phone=phone2,message=message2).save()
    
    return render(request,'contact.html')
def myfunc5(request):
    topics1=Subjects.objects.all()
    return render(request,'topics.html',{"topics1":topics1})
def myfunc6(request,Subjects_id):
    material=Subjects.objects.get(id=Subjects_id)
    return render(request,'topics_detail.html',{'material':material})

