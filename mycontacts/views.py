from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def contacts(requests):
    return HttpResponse('Your contact list is empty.')
def friends(requests): 
    return HttpResponse('Your friends list is empty.')
