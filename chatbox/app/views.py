from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

class Register(View):
    def get(self, request):
        # 判断是否登录
        message = request.GET.get('message', '')
        if request.user.is_authenticated:
            return redirect('/index')
        return render(request, 'register.html', {'message':message})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        check_password = request.POST.get('check_password', '')
        if password != check_password:
            return redirect('/register?message=输入密码与确认密码不一致')
        # 判断是否注册过
        exists = User.objects.filter(username=username).exists()
        if exists:
            return redirect('/register?message=该账号已注册')
        User.objects.create_user(username=username, password=password)
        return redirect('/login')


class Login(View):
    def get(self, request):
        message = request.GET.get('message', '')
        return render(request, 'login.html', {'message':message})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return redirect('/login?message=该账号不存在')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/index')
        else:
            return redirect('/login?message=用户名密码错误')


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    def post(self, request):
        pass 


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')

    def post(self, request):
        pass 
