from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import User
def index(request):
    res = User.objects.all()
    print(res)
    return HttpResponse("Hello, world. You're at the polls index.")