from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
import json

from .models import *

# Create your views here.
def stor(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, camplate=False)
        itims = order.ordertime_set.all()
        cartItms = order.get_cart_items
    else:

        itims = []
        order = { 'get_cart_items':0, 'get_card_total':0,  'shipping': False }
        cartItms = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItms': cartItms, 'itims': itims}
    return render(request, 'storee/stor.html', context)
def main(request):
    context ={}
    return render(request, 'storee/main.html', context)
    
def card(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, camplate=False)
        itims = order.ordertime_set.all()
        cartItms = order.get_cart_items
    else:

        itims = []
        order = { 'get_cart_items':0, 'get_card_total':0,  'shipping': False  }
        cartItms = order['get_cart_items']

    context = {'itims': itims, 'order': order, 'cartItms': cartItms}
    return render(request, 'storee/card.html', context )
    
# def shop(request):
#     context ={}
#     return render(request, 'storee/shop_stor.html', context)
    
def checout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, camplate=False)
        itims = order.ordertime_set.all()
        cartItms = order.get_cart_items

    else:

        itims = []
        order = { 'get_cart_items':0, 'get_card_total':0, 'shipping': False }
        cartItms = order['get_cart_items']

    context = {'itims': itims, 'order': order, 'cartItms': cartItms}
    return render(request, 'storee/checout.html', context)
    



def updeteitm(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:',action)
    print('Productid',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, camplate=False )

    orderItem, created = Ordertime.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()



   

    # customer = request.user.customer
    # product = Product.objects.get(id=productId)
    # order, created = Order.objects.get_or_create(customer=customer, camplate=False)

    # orderItem = created = Ordertime.objects.get_or_create(order=order, product=product)

    # if action == 'add':
    #     orderItem.quantity = (orderItem.quantity + 1) 
    # elif action == 'remove':
    #     orderItem.quantity = (orderItem.quantity - 1)

    # orderItem.save()

    

    # if orderItem.quantity <= 0:
    #     orderItem.delete()
    return JsonResponse('Item was added', safe=False)   



# def malumotqoshish(request):
#     if request.method == 'POST':
#         form = Malumotforms(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('tushganpul')
#     else:
#         form = Malumotforms()
        
    
#     return render(request, 'storee/checout.html.html', {'form': form})

# def kelganpul(request,):
#     som = Malumotjonat.objects.all()
#     context = {'som':som,}
#     return render(request,'storee/tushganmakumot.html', context)

    

