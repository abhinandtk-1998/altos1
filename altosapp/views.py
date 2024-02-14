from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    item_id = request.GET.get('item_id')
    return render(request, 'second_page.html', {'item_id': item_id})

