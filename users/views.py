from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password = password)
        if user is not None:
            print("인증성공")
            login(request,user)
        else:
            print("인증실패")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        # 사용자 이름(username)이 이미 존재하는지 확인
        if User.objects.filter(username=username).exists():
            return render(request, "users/signup.html", {"error": "이미 사용 중인 사용자 이름입니다."})

        user = User.objects.create_user(username, email, password)
    #     user.last_name = lastname
        user.save()
        return redirect("user:login")

    return render(request, "users/signup.html")