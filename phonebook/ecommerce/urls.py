from django.contrib import admin
from django.urls import path,include

from ecommerce import views

app_name = 'ecommerceapp'

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login,name="login"),
    path('delete/<int:p>',views.delete,name="delete"),
    path('update/<int:p>',views.update,name="update"),
    path('Register',views.Register,name="Register"),
    path('product',views.product,name="product"),
    path('prodcreate',views.prodcreate,name="prodcreate"),
    path('rodcreate',views.rodcreate,name="rodcreate"),
    path('productupdate/<int:p>',views.productupdate,name="productupdate"),
    path('productdelete/<int:p>',views.productdelete,name="productdelete"),
    path('toshowcategory/<str:p>',views.toshowcategory,name="toshowcategory"),
    path('showallproduct/<int:p>',views.showallproduct,name="showallproduct"),
    path('atleastorder',views.atleastorder,name="atleastorder"),
    path('atleastorderuser',views.atleastorderuser,name="atleastorderuser"),
    path('rodcreate',views.rodcreate,name="rodcreate"),
]