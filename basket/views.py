from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ A view that returns basket page and its contents """
    return render(request, 'basket/basket.html')
