from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from icecream.models import Signup
from icecream.models import Login
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def home(request):
    return render(request, 'Intext.html')

def about(request):
    return render(request, 'Aboutus.html')
def event(request):
    return render(request, 'event.html')
def login(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/signup.html")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
            login.save()
    return render(request, 'login.html')

    # def logoutUser(request):
        # logout(request)
        # return redirect("/login")
    # return render(request, 'login.html')


def signup(request):
    if request.method =="POST":
        username = request.POST.get('username1')
        email1 = request.POST.get('email')
        password= request.POST.get('password1')
        # comform = request.POST.get('conpassward')
        signup = Signup(username=username, email1=email1, password=password)
        signup.save()
        messages.success(request, "your massage has been sent!!")
    return render(request, 'signup.html')

# def login(request):
#     if request.method =="POST":
#         username = request.POST.get('username')
#         password= request.POST.get('password')
       
#         login= Login(username=username, password=password)
#         login.save()
#         messages.success(request, "your massage has been sent!!")
#     return render(request, 'signup.html')


