from django.contrib import admin
from django.urls import path,include

from todoapp1 import views

app_name = 'todoapp1'

urlpatterns = [
    path('createtodo',views.createtodo,name="createtodo"),
    path('show',views.show,name="show"),
    path('changetodo/<int:p>',views.changetodo,name="changetodo")
]