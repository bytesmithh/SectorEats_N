from django.urls import path
from . import views
from .views import admin_dashboard

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),
    path("delete_restaurant/<int:rid>/", views.delete_restaurant, name="delete_restaurant"),
    path("edit_restaurant/<int:rid>/", views.edit_restaurant, name="edit_restaurant"),
    # path('admin/dashboard/', views.admin_dashboard, name='admin-dashboard'),
]
