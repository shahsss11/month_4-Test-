from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories_list, name='categories'),
    path('products/', views.products_list, name='products_list'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
]