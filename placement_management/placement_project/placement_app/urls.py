from django.urls import path

from . import views

urlpatterns = [

    path('', views.home),

    path('register/', views.register),

    path('login/', views.login),

    path(
        'apply/<str:company_id>/',
        views.apply_company
    ),

    path(
        'withdraw/<int:application_id>/',
        views.withdraw_application
    ),

    path(
        'admin-login/',
        views.admin_login
    ),

    path(
        'add-company/',
        views.add_company
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard
    ),
]