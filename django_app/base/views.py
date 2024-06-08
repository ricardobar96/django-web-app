from django.shortcuts import render
from django.http import HttpResponse

def list_orders(order):
    return HttpResponse('Orders')
