from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as denis_views

urlpatterns = [
    path('register/', denis_views.register, name='register-url'),
    path('all_members/', denis_views.all_members, name='all_members'),
    path('milk_record/', denis_views.record_milk, name='milk_record'),
    path('calculate_amount/', denis_views.calculate_amount, name='calculate_amount'),
    path('choose_activity/', denis_views.choose_activity, name='choose_activity'),
]
