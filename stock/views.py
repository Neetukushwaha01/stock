from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Stack

from django.contrib.auth.models import User

# Create your views here.

def signup_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        u =User.objects.create_user(username=username,password=password,email=email)
        if u:
            print("User created successfully")
            return redirect('login')
    return render(request, 'signup.html', context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            context['msg'] = 'Done'
            return redirect('/')
        else:
            context['msg'] = 'Sorry your Password was worng'
    return render(request, 'login.html', context)


def home_view(request):

    contex={}
    if not request.user.is_authenticated:
        return redirect('login')
    stock_list = Stack.objects.all().order_by('-id')[0:5]
    if 'extra' in request.GET:
        contex['more']=True
        stock_list = Stack.objects.all().order_by('-id')
    if 'sbtn' in request.GET:
        skey =request.GET.get('search_key')
        stock_list = Stack.objects.filter(stock_name__startswith=skey).order_by('-id')
    contex['list']=stock_list


    return render(request, 'home.html',contex)

def logout_view(request):
    logout(request)

    return redirect('login')



def view_page(request,slug=None):
    contex = {}
    one_rec = Stack.objects.get(slug=slug)
    print(one_rec)

    contex['view_list'] = one_rec



    return render(request,'view_page.html',contex)