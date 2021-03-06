from django.contrib.auth import logout,login ,authenticate
from django.shortcuts import render, HttpResponseRedirect

from .forms import LoginForm ,RegistrationFrom
# Create your views here.


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        login(request,user)
        return HttpResponseRedirect("/")



    context = {
        "form":form
    }
    return render(request,"form.html" , context)

def registration_view(request):
    form = RegistrationFrom(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.first_name = "Bhavit"
        new_user.save()
        # username = form.cleaned_data["username"]
        # password = form.cleaned_data["password"]
        # user = authenticate(username=username, password=password)
        # login(request,user)
        pass

    context = {
        "form":form
    }
    return render(request,"reg_form.html" , context)