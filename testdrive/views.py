#-*- encoding: utf-8 -*-
# from django.shortcuts import render
from Car.forms import TestDriveForm
from Car.models import Car
from testdrive.models import TestDrive
from django.contrib.auth.models import User,auth
from django.shortcuts import render_to_response, redirect,HttpResponse
from django.core.context_processors import csrf
# Create your views here.


def add_test_drive(request):
    args={}
    args.update(csrf(request))
    args['car'] = Car.objects.all()

    if request.POST:
        de=TestDrive(car= Car.objects.get(id=request.POST.get('ComboBox','')),
                     user=User.objects.get(id= auth.get_user(request).id),
                     date_completed=request.POST.get('min',''))
        de.save()
        args['word'] = "Спасибо за запись на тест-драйв!"
    args['username'] = auth.get_user(request).username
    return render_to_response('testdrive.html',args)

def delete_test_drive(request,id_service):
    args={}
    args.update(csrf(request))
    de = TestDrive.objects.get(id=id_service)
    de.delete()
    return redirect('/order/cart/')