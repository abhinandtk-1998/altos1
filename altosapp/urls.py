from django.urls import path,include
from .import views

urlpatterns = [
    path('first-page/', views.first_page, name='first_page'),
    path('second-page/',views.second_page,name='second_page'),
    path('move-to-basket/', views.move_to_basket, name='move_to_basket'),
]