from django.urls import path
from .import views
app_name='account'
urlpatterns = [
    path('register', views.register, name='reg'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    ]