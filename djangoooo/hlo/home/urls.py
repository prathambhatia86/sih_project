from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name ='home'),
        path("contact",views.Contact,name ='Contact'),
          path("cop",views.cop,name ='cop'),
           path("home",views.index,name ='home')
]
 