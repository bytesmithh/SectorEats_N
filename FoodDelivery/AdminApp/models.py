from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=50)
    role = models.CharField(max_length=10, default="user")  # admin/user
    
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set", blank=True)


class Restaurant(models.Model):
    rname = models.CharField(max_length=50)
    raddress = models.CharField(max_length=100)
    image_filename = models.ImageField(upload_to="restaurants/", null=True, blank=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menu_items")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=20, default="Pending")
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.quantity * item.price for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="order_items")
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_items")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField()


class AdminUser(models.Model):  # Example admin user model
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username  