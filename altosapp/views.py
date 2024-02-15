from django.shortcuts import render

# Create your views here.

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    item_ids = request.GET.get('item_ids', '').split(',')
    return render(request, 'second_page.html', {'item_ids': item_ids})

