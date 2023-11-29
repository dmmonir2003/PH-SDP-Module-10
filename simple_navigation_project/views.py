from django.shortcuts import render


def rootcall(request):
    
    return render(request,'index.html')