from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("Welcome to Django!!")

def test_html(request):
    return render(request,"test.html")