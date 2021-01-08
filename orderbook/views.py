from django.shortcuts import render
from . import models


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def get_data():
    askorders = models.get_ask_orders()
    bidorders = models.get_bid_orders()
    return askorders, bidorders


a_orders, b_orders = get_data()
context = {'askorders': a_orders[:5][::-1], 'bidorders': b_orders[:5]}


def shares(request):
    global context
    return render(request, 'shares.html', context)


def marketorder(request):
    global context
    return render(request, 'marketorder.html', context)


def limitorder(request):
    global context
    return render(request, 'limitorder.html',context)


def feedback(request):
    return render(request, 'feedback.html')


def morder(request):
    global a_orders, b_orders
    a_orders = iter(a_orders)
    b_orders = iter(b_orders)

    askorders = []
    while len(askorders) != 5:
        askorders.append(next(a_orders))
    
    bidorders = []
    while len(bidorders):
        bidorders.append(next(b_orders))

    shares = request.GET.get('share')
    operation = request.GET.get('flexRadioDefault')

    if operation == 'buy':
        orders = askorders[::-1]
        for i in range(len(orders)):
            orders[i].size -= int(shares)
            if orders[i].size >= 0:
                break
            else:
                shares = abs(orders[i].size)
                del orders[i]
                continue
    else:
        pass

    while len(askorders) != 5:
        askorders.append(next(a_orders))
    
    while len(bidorders):
        bidorders.append(next(b_orders))

    my_context = {'askorders': askorders[::-1], 'bidorders': context['bidorders']}
    return render(request, 'order.html', context=my_context)
