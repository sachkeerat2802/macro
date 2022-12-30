from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('user/overview/', views.user_overview, name="overview"),
    path('user/account/', views.view_account, name="account"),
    path('user/account/edit/', views.edit_account, name="edit-account"),
    path('weight/edit/<str:pk>/', views.weight_edit, name="edit-weightlog"),
    path('weight/delete/<str:pk>/', views.weight_delete, name="delete-weightlog"),
]
