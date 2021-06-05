from django.urls import path, include
from menu_gusto.views import *

urlpatterns = [
    path('<int:pk>', dish_info),
    path('categories/',categories),
    path('dishes/',dishes),
    path('create_dish/', create_dish),
    path('edit_dish/<int:pk>',edit_dish),
    path('delete_dish/<int:pk>',delete_dish),
    path('create_category/', create_category),
    path('edit_category/<int:pk>',edit_category),
    path('delete_category/<int:pk>',delete_category)
]