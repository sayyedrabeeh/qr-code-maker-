from django.contrib import admin
from django.urls import path
from .views import index,generate_qr

print('qrapp urls.py')

urlpatterns = [
    
    path('',index,name='index'),
    path('generate_qr/',generate_qr,name='generate_qr')

]