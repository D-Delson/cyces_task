from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('products_add/', views.ProductCreateView.as_view(), name='product_add'),
    path('products_update/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),

    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category_add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category_update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('subcategory/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory_add/', views.SubCategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory_update/<int:pk>', views.SubCategoryUpdateView.as_view(), name='subcategory_update'),
    path('subcategory_delete/<int:pk>', views.SubCategoryDeleteView.as_view(), name='subcategory_delete')
]