from django.urls import path,include
from .import views

urlpatterns = [
    # path('', views.first_page, name='first_page'),
    # path('second_page/', views.second_page, name='second_page'),
    path('', views.page1, name='page1'),
    path('page2',views.page2, name='page2'),

]