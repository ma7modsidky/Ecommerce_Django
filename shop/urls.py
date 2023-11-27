from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('search/', views.product_search,
         name='product_search'),

    path('products/', views.product_list, 
            name='product_list'),


    path('products/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),


    path('about_us/', views.about_us.as_view(),
         name='about_us'),

    path('contact_us/', views.contact_us.as_view(),
         name='contact_us'),

    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),

    path('', views.home,
         name='home'),

]
