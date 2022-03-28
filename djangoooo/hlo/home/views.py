from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User

def index(request):
    if request.method=="POST":
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        cp=request.POST.get('cp')
        appid=request.POST.get('appid')
        mobno=request.POST.get('mobno')
        coach=request.POST.get('coach')
        scid=request.POST.get('scid')
        myuser=User.objects.create_user(un,pw,appid,mobno,coach,scid)
    return render( request , "home.html")
def Contact(request):
    return render( request , "Contact.html")
def cop(request):
    return render( request , "cop.html")
def account(request):
    return render( request , "account.html")    



