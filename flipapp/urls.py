from django.urls import path
from .import views
app_name='flipapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('details', views.prodDetails, name='details'),
    path('<slug:c_slug>/', views.home, name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('search', views.search, name='search'),

    ]