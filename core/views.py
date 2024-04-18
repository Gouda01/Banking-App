from django.shortcuts import render


# Create your views here.

def burito(request):
    return render(request,'core/index.html')