from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products_add/', views.product_add, name='product_add'),
    path('products_update/<int:i>', views.product_update, name='product_update'),
    path('product_delete/<int:i>', views.product_delete, name='product_delete'),

    path('category/', views.category_list, name='category_list'),
    path('category_add/', views.category_add, name='category_add'),
    path('category_update/<int:i>', views.category_update, name='category_update'),
    path('category_delete/<int:i>', views.category_delete, name='category_delete'),

    path('subcategory/', views.subcategory_list, name='subcategory_list'),
    path('subcategory_add/', views.subcategory_add, name='subcategory_add'),
    path('subcategory_update/<int:i>', views.subcategory_update, name='subcategory_update'),
    path('subcategory_delete/<int:i>', views.subcategory_delete, name='subcategory_delete')
]