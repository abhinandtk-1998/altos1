from django.shortcuts import render

# Create your views here.

# def first_page(request):
#     item_idf = request.GET.get('item_idf',' ').split(',')
#     return render(request, 'first_page.html',{'item_idf': item_idf})

# def second_page(request):
#     item_ids = request.GET.get('item_ids',' ').split(',')
#     return render(request, 'second_page.html', {'item_ids': item_ids})

def page1(request):
    return render(request, 'page1.html')


