from datetime import datetime
from tabnanny import check
from urllib.robotparser import RequestRate
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from .models import User
from .forms import signupform
from django.contrib import messages #import messages
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


# Create your views here.

# def thankyou(request):
#     # return render (request, 'profile.html')

# def welcome(request):
#     # return render (request, 'login.html')


def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        # value = User.objects.filter(username= 'aatish')
        return render(request, 'base.html', param)
    
    else:
        return redirect('login')


# def signup(request):
#     form= regform(request.POST)
#     if form.is_valid():
#         uname = form.cleaned_data['uname']
#         # email = form.cleaned_data['email']
#         pwd = make_password(form.cleaned_data['pwd'])

#         # if password and confirmpassword and password != confirmpassword:
#         #     messages.warning(request, 'password error')
#         #     return redirect('/')

#         # if User.objects.filter(email=email).exists():
#         #     messages.warning(request, 'user already exists')
#         #     return redirect('signup')

#         if User.objects.filter(username=uname).count()>0:
#             return HttpResponse('username already exists.')

#         else:
#             data= User(username=uname, password=pwd)
#             data.save()
#             return redirect('login')
#     # else:
#     #     form = regform()

#     # context = {'form':form}
#     # return render(request,'signup.html',context)

#     else:
#         return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        rpwd = request.POST.get('rpwd')

        if pwd != rpwd:
            messages.error(request,'password did not match', extra_tags='match')
            return redirect('signup')

        if User.objects.filter(username=uname).count()>0:
            messages.error(request,'Username already exists.', extra_tags='username')
            return redirect('signup')
        
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')


# def login(request):
#     if request.method == 'POST':
#         form= loginform(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = make_password(form.cleaned_data['password'])

#             check_user = User.objects.filter(email=email, password=password)

#             if check_user:
#                 request.session['user'] = email
#                 return redirect('home')

#             else:
#                 return HttpResponse('please enter valid username and password')

#     return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('chk')

        check_user = User.objects.filter(username=uname, password=pwd)

        if remember and check_user :
            request.session['user'] = uname
            request.session.set_expiry(864000)
            return redirect('home')

        if check_user:
            request.session['user'] = uname
            return redirect('home')    

        else:
            messages.error(request, 'check your username or password')

    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
        
    except:
        return redirect('login')
    return redirect('login')

def editprofile(request):
    return render(request, 'edit.html')
    


def changepass(request):
    if request.method == 'POST':
        old_pass = request.POST.get('old_pwd')
        new_pass = request.POST.get('new_pwd')


        check_user = User.objects.filter( password=old_pass).exists()

        if check_user:
            user = User(password=new_pass)
            user.save()
            return redirect('home')













# COOKIES

def setcookie(request):
    response = render(request, 'setcookie.html')
    # response.set_cookie('name', 'aatish', max_age = 5)
    # response.set_cookie('name', 'aatish', expires=datetime.utcnow()+timedelta(days=2))
    response.set_signed_cookie('name', 'aatish',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('name', "guest")
    # name = request.get_signed_cookie('name', salt = 'nm')
    name = request.get_signed_cookie('name',default= 'Guest' ,salt = 'nm')
    return render(request, 'getcookie.html', {'name': name})


def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response



# SESSIONS

def setsession(request):
    request.session['name'] = 'aatish'
    request.session['lname'] = 'vaid'
    return render(request, 'setsession.html')

def getsession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    # age = request.session.setdefault('age', '26')
    # return render(request, 'getsession.html', {'name':name, 'lname': lname, 'keys':keys, 'items':items, 'age':age})
    return render(request, 'getsession.html', {'name':name, 'lname': lname, 'keys':keys, 'items':items})

def delsession(request):
    # if 'name'in request.session:
        # del request.session['name']
    request.session.flush()
    return render(request, 'delsession.html')





    # if request.POST:
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     password = request.POST['password']

    #     form = regform(request.POST)

    #     if form.is_valid():
    #         check_existing = User.objects.filter(email=email) or User.objects.filter(password=password).exists()
    #         if check_existing:
    #             messages.success(request, 'user already exists')
    #             return redirect('signup')

    #         else:
    #             data = User(name=name, email=email, password=password)
    #             data.save()
    #             messages.success(request, 'successfully save')
    #             return redirect('signup')

    # else:
    #     form = regform()
    #     context = {'form':form}
    #     return render(request,'index.html',context)


# MIDDLEWARE

def midware(reqeust):
    print('I am view')

    return HttpResponse("this is home page")