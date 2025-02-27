from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    is_active = models.BooleanField(default=True)  # Boolean field with a default value
    wallet_balance = models.DecimalField(
        max_digits=10,  # Total number of digits (including decimal places)
        decimal_places=2,  # Number of decimal places
        default=0.00
    )

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)  # Category name
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation

    def __str__(self):
        return self.name

class Product(models.Model):
    name =  models.CharField(max_length=100)
    price =  models.DecimalField(
        max_digits=10,  # Total number of digits (including decimal places)
        decimal_places=2,  # Number of decimal places
        default=0.00
    )
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='itemsuser')
    total_price = models.DecimalField(
        max_digits=10,  # Total number of digits (including decimal places)
        decimal_places=2,  # Number of decimal places
        default=0.00
    )
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items1')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items2')
    quantity = models.IntegerField()
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.product.name} x {self.quantity} (Subtotal: {self.subtotal_price})"


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('wallet', 'Wallet'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    order = models.OneToOneField(OrderItem, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, unique=True)
    paid_at = models.DateTimeField(null=True, blank=True)






