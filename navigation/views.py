from django.shortcuts import render

# Create your views here.


def home(request):

    d={'name':'monir','age':1,'marks':[60,40,19,40],'course':[
        {
            "id":1,
            "name":"python",
            "fee":5000
        },
        {
            "id":2,
            "name":"C++",
            "fee":1000
        },
        {
            "id":1,
            "name":"django",
            "fee":5600
        },
    ]}

    return render(request,'navigation/home.html',d)
def about(request):
    return render(request,'navigation/about.html')
def contact(request):
    return render(request,'navigation/contact.html')