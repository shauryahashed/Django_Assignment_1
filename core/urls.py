from django.urls import path
from .views import CartItemDetailView, CartItemListCreateView, RegisterView
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

urlpatterns = [
        
        path('register/', RegisterView.as_view(), name='register'),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('cart/', CartItemListCreateView.as_view(), name='cart_list_create'),
        path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart_detail'),
    ]