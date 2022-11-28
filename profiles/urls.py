from django.urls import path

from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_hisrtory/<order_number>', views.order_history,
         name='order_history'),
    path('edit_profile/', views.EditUserProfile, name='edit_user_profile'),
    path('password/', views.ChangePassword, name='change_password'),
    path('wishlist/add_to_wishlist/<int:product_id>',
         views.add_to_wishlist, name="user_wishlist"),
]
