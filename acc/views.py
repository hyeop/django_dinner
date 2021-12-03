from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
# messages.info(request, "정보가 수정되었습니다.")

def remove(request):
    request.user.delete()
    return redirect("acc:login")


def update(request):
    print(request.user.check_password("123"))
    if request.method == "POST":
        user = request.user
        pw = request.POST.get("password")
        ni = request.POST.get("nickname")
        co = request.POST.get("comment")
        pi = request.FILES.get("pic")
        if pw:
            user.set_password(pw)
        user.nickname = ni
        user.comment = co
        if pi:
            user.pic.delete()
            user.pic = pi
        user.save()
        login(request, user)
        messages.info(request, "정보가 수정되었습니다.")
        return redirect("acc:profile")

    return render(request, "acc/update.html")

def profile(request):
    return render(request, "acc/profile.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(username=un, password=pw)
        if user:
            print(user)
            login(request, user)
            messages.success(request, f"{request.user.username} 님 안녕하세요~")
            return redirect("acc:index")
        else:
            messages.error(request, "로그인 실패 :(")
    return render(request, "acc/login.html")


def index(request):
    return render(request, "acc/index.html")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("username")
        if not User.objects.filter(username=un):
            pw = request.POST.get("password")
            ni = request.POST.get("nickname")
            co = request.POST.get("comment")
            pi = request.FILES.get("pic")
            User.objects.create_user(username=un, password=pw, nickname=ni, comment=co, pic=pi)
            messages.success(request, "계정이 생성되었습니다. 로그인해주세요.")
            return redirect("acc:login")   
        else:
            messages.error(request, "계정이름 중복!!")
    return render(request, "acc/signup.html")

