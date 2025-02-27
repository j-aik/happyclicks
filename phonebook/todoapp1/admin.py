from django.contrib import admin

# Register your models here.





from ecommerce.models import  Category, Product, Order, OrderItem, Payment

# Register all models

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
