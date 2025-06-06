from calendar import error

from django.shortcuts import render, redirect
from django.template.context_processors import request

from Harmony.models import users, admin, state, city, bloodgroup


# Create your views here.

def home(req):
    return render(req,'home.html')

def about(req):
    if req.method =='POST':
        pass
    else:
        return render(req,'about.html')

def contact(req):
    if req.method =='POST':
        pass
    else:
        return render(req,'contact.html')

def welcome(req):
    return render(req,'adminwelcome.html')


def register(req):
    if req.method =='POST':
        a = req.POST.get('uname')
        b = req.POST.get('pwd')
        j=req.POST.get('cpwd')
        c = req.POST.get('gender')
        d = req.POST.get('languages')
        e = req.POST.get('state')
        f = req.POST.get('city')
        g = req.POST.get('bloodgroup')
        h = int(req.POST.get('phno'))
        i = req.POST.get('email')
        special_characters = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
        if b != j:
            return render(req, 'register.html', {'msg': 'Password and Confirm Password should be the same.'})
        if not any(char.isupper() for char in b):
            return render(req, 'register.html', {'msg': 'Password must contain at least one uppercase letter.'})
        if not any(char.isdigit() for char in b):
            return render(req, 'register.html', {'msg': 'Password must contain at least one number.'})
        if not any(char in special_characters for char in b):
            return render(req, 'register.html', {'msg': 'Password must contain at least one special character.'})
        if len(b) < 8 or len(b) > 12:
            return render(req, 'register.html', {'msg': 'Password must be between 8 and 12 characters long.'})
        d1 = users(user_name=a, password=b, gender=c, languages=d,  state=e, city=f, blood_group=g, phone_number=h, email=i)
        d1.save()
        res1 = state.objects.all().values_list('state_name', flat=True)
        res2 = city.objects.all().values_list('city_name', flat=True)
        res3 = bloodgroup.objects.all().values_list('bloodgroup_name', flat=True)
        return render(req, 'register.html', {'msg': 'Successfully Registered. Proceed to Login','res1':res1,'res2':res2,'res3':res3})
    else:
        res1=state.objects.all().values_list('state_name', flat= True)
        res2=city.objects.all().values_list('city_name', flat= True)
        res3=bloodgroup.objects.all().values_list('bloodgroup_name', flat= True)
        return render(req,'register.html',{'res1':res1,'res2':res2,'res3':res3})

def adminlogin(req):
    if req.method =='POST':
        try:
            a =req.POST.get('uname')
            b= req.POST.get('pwd')
            c=admin.objects.get(admin_id=a)
            if c.password == b:
                return render(req, 'adminwelcome.html')
            else:
                error = 'Invalid Credentials1'
                return render(req, 'adminlogin.html', {'error': error})
        except:
            error='Invalid Credentials2'
            return render(req,'adminlogin.html',{'error':error})
    else:
        return render(req,'adminlogin.html')


def admindetails(req):
    res=users.objects.all()
    return render(req,'admindetails.html',{'res':res})

def deleterecord(req,user_id):
    res=users.objects.get(user_id=user_id)
    res.delete()
    return redirect(admindetails)

def updaterecord(req,user_id):
    res=users.objects.get(user_id=user_id)
    return render(req,'adminupdate.html',{'user':res})


def update(req):
    if req.method == 'POST':
        g=request.POST.get('user_id')
        a= request.POST.get('user_name')
        b=request.POST.get('blood_group')
        c=request.POST.get('phone_number')
        d=request.POST.get('email')
        e=request.POST.get('city')
        f=users.objects.get(user_id=g)
        f.user_name=a
        f.blood_group=b
        f.phone_number=c
        f.email=d
        f.city=e
        f.save()
        return redirect('admindetails')


def adminsearch(req):
    res1 = state.objects.all().values_list('state_name', flat=True)
    res2 = city.objects.all().values_list('city_name', flat=True)
    res3 = bloodgroup.objects.all().values_list('bloodgroup_name', flat=True)
    if req.method =='POST':
        try:
            a = req.POST.get('bloodgroup')
            b=req.POST.get('state')
            c=req.POST.get('city')
            d = users.objects.filter(blood_group=a,state=b,city=c)
            if d:
                return render(req, 'adminsearch.html', {'details': d,'res1':res1,'res2':res2,'res3':res3})
            else:
                return render(req, 'adminsearch.html', {'error': 'No Users Found','res1':res1,'res2':res2,'res3':res3})
        except:
            return render(req, 'adminsearch.html',
                   {'error': 'No Users found', 'res1': res1, 'res2': res2, 'res3': res3})
    else:
        return render(req,'adminsearch.html',{'res1':res1,'res2':res2,'res3':res3})


def userloign(req):
    if req.method =='POST':
        try:
            a = req.POST.get('uname')
            b = req.POST.get('pwd')
            c = users.objects.get(user_name=a)
            if c.password == b:
                return render(req, 'userwelcome.html',{'res':a})
            else:
                error = 'Invalid Credentials1'
                return render(req, 'userlogin.html', {'error': error})
        except:
            error = 'Invalid Credentials2'
            return render(req, 'userlogin.html', {'error': error})
    else:
        return render(req,'userlogin.html')


def userwelcome(req):
    return render(req,'userwelcome.html')

def userupdate(req):
    return render(req,'userupdate.html')

def usersearch(req):
    res1 = state.objects.all().values_list('state_name', flat=True)
    res2 = city.objects.all().values_list('city_name', flat=True)
    res3 = bloodgroup.objects.all().values_list('bloodgroup_name', flat=True)
    if req.method =='POST':
        try:
            a = req.POST.get('bloodgroup')
            b=req.POST.get('state')
            c=req.POST.get('city')
            d = users.objects.filter(blood_group=a,state=b,city=c)
            if d:
                return render(req, 'usersearch.html', {'details': d,'res1':res1,'res2':res2,'res3':res3})
            else:
                return render(req, 'usersearch.html', {'error': 'No transactions found for this Customer ID','res1':res1,'res2':res2,'res3':res3})
        except:
            return render(req, 'usersearch.html',
                   {'error': 'No transactions found for this Customer ID', 'res1': res1, 'res2': res2, 'res3': res3})
    else:
        return render(req,'usersearch.html',{'res1': res1, 'res2': res2, 'res3': res3})


def logout(req):
    return render(req,'logout.html')