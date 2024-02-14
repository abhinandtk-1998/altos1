from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Basket, Item

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    return render(request, 'second_page.html')

def move_to_basket(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        # Update database: move item to basket
        return HttpResponseRedirect('/second-page/')  # Redirect to second page
    else:
        return HttpResponseRedirect('/first-page/')  # Redirect back if not a POST request


