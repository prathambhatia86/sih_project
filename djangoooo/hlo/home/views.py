from django.shortcuts import render,HttpResponse

def index(request):
    return render( request , "home.html")
def Contact(request):
    return render( request , "Contact.html")
def cop(request):
    return render( request , "cop.html")



