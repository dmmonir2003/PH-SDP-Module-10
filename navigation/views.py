from django.shortcuts import render

# Create your views here.


def home(request):

    d={'name':'monir','age':12,'marks':[60,40,19,40]}

    return render(request,'navigation/home.html',d)
def about(request):
    return render(request,'navigation/about.html')
def contact(request):
    return render(request,'navigation/contact.html')