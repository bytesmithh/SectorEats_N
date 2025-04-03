from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, MenuItem, Order, OrderItem, Cart

@login_required
def admin_dashboard(request):
    context = {
        'current_user': request.user,  
        }
    return render(request, 'admin_dashboard.html', context)

@login_required
def delete_restaurant(request, rid):
    restaurant = get_object_or_404(Restaurant, id=rid)
    restaurant.delete()
    messages.success(request, "Restaurant deleted successfully!")
    return redirect("admin_dashboard")

@login_required
def edit_restaurant(request, rid):
    restaurant = get_object_or_404(Restaurant, id=rid)
    return render(request, "add_restaurant.html", {"restaurant": restaurant})


# def admin_dashboard(request):
#     return render(request, 'dmin_dashboard.html')