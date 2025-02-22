from django.contrib import admin
from django.urls import path,include

from bookapp import views

app_name = 'bookapp'

urlpatterns = [
    path('',views.home,name="home"),
    path('phonebookadd',views.phonebookadd,name="phonebookadd"),
    path('phonebookadded',views.phonebookadded,name="phonebookadded"),
    path('phonebookedit/<int:p>',views.phonebookedit,name="phonebookedit"),
    path('uudelete/<int:p>',views.uudelete,name="uudelete")

]