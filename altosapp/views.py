from django.shortcuts import render

# Create your views here.


def page1(request):
    item_idf = request.GET.get('item_idf',' ').split(',')
    return render(request, 'page1.html',{'item_idf':item_idf})

def page2(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'page2.html', {'item_ids': item_ids})



