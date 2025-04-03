from django.contrib import admin
from .models import User, Restaurant, MenuItem, Order, OrderItem, Cart, AdminUser

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(AdminUser)
