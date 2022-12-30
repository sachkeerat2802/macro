from django.urls import path
from . import views
from user import views as user_views

urlpatterns = [
    path('view/<str:pk>/', views.view_food, name="food"),
    path('add/', views.add_food, name="add-food"),
    path('list/', views.food_list, name="food-list"),
    path('edit/<str:pk>/', views.edit_food, name="food-edit"),
    path('delete/<str:pk>/', views.delete_food, name="food-delete"),
    path('log/delete/all/', user_views.clear_foodlogs, name="foodlogs-clear"),
    path('log/delete/<str:pk>/', user_views.delete_foodlog, name="foodlog-delete"),
]
