from django.shortcuts import render,render_to_response,redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
#from logsys.user_reg import UserCreationForm
from Car.forms import Registration
# Create your views here.
#-*- encoding: utf-8 -*-
def login(reguest):
    args = {}
    args.update(csrf(reguest))
    if reguest.POST:
        username = reguest.POST.get('username', '')
        password = reguest.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(reguest, user)
            return redirect('/')
        else:
            args['login_error']= "Error"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(reguest):
    auth.logout(reguest)
    return redirect("/")

def register(reguest):
    args = {}
    args.update(csrf(reguest))
    args['form'] = UserCreationForm()
    if reguest.POST:
        username = reguest.POST.get('username', '')
        password2 = reguest.POST.get('password2', '')
        email = reguest.POST.get('email', '')
        first_name = reguest.POST.get('first_name', '')
        last_name = reguest.POST.get('last_name', '')

        new_user_form = UserCreationForm(reguest.POST)
        new_user_form.save()
        new_user = auth.authenticate(username= username,
                                      password= password2,
                                      email=email,
                                      first_name=first_name,
                                      last_name=last_name
                                        )

        auth.login(reguest, new_user)
        args['word']= "Thank you for registering"
        args['form']= new_user_form
    return render_to_response('register.html', args)

