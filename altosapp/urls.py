from django.urls import path,include
from .import views

urlpatterns = [
    path('first_page', views.first_page, name='first_page'),
    path('second_page', views.second_page, name='second_page'),
    path('about_us',views.about_us,name='about_us'),
]