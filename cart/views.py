from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cart_details(request,tot=0,count=0,ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        print(ct)
        ct_items = cart_items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot += (i.prodt.price*i.quatity)
            count += i.quatity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
       c_item = cart_items.objects.get(prodt=prod,cart=ct)
       if c_item.quatity < c_item.prodt.stock:
           c_item.quatity+=1
       c_item.save()
    except cart_items.DoesNotExist:
        c_item = cart_items.objects.create(prodt=prod,quatity=1,cart=ct)
        c_item.save()
    return redirect('cartDetails')

def min_cart(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products,id=product_id)
    c_items = cart_items.objects.get(prodt=prod,cart=ct)
    if c_items.quatity>1:
        c_items.quatity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = cart_items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')
