from django.shortcuts import render
from django.shortcuts import render_to_response, redirect,HttpResponse
from django.core.context_processors import csrf
from Car.models import Car
from order.models import Cart
from django.contrib.auth.models import User,auth
from django.template import RequestContext
from checkup.models import Checkup
from testdrive.models import TestDrive

def cart(request):
    return render_to_response('cart.html',
                              {'form': Cart.objects.filter(user=User.objects.get(id= auth.get_user(request).id)),
                               'checkup':Checkup.objects.filter(user=User.objects.get(id= auth.get_user(request).id)),
                               'testdrive':TestDrive.objects.filter(user=User.objects.get(id= auth.get_user(request).id)),
                              'username': auth.get_user(request).username},
        context_instance=RequestContext(request)
    )

def add_cart(reguest):
    args={}
    args.update(csrf(reguest))
    if reguest.POST:
        args['car'] = Car.objects.get(id=reguest.POST.get('id',''))
        de=Cart(vehicle= Car.objects.get(id=reguest.POST.get('id','')),
                user=User.objects.get(id= auth.get_user(reguest).id),
                quantity=reguest.POST.get('quantity',''))
        de.save()
        args['word'] = "asdasd"
    return redirect('/order/cart/')

def delete_cart(request,id_cart):
    args={}
    args.update(csrf(request))
    de = Cart.objects.get(id=id_cart)
    de.delete()
    return redirect('/order/cart/')