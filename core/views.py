from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import generics, permissions
from .models import CartItem
from .serializers import CartItemSerializer

class RegisterView(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer



# Create your views here.
class CartItemListCreateView(generics.ListCreateAPIView):
        queryset = CartItem.objects.all()
        serializer_class = CartItemSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
            return self.queryset.filter(user=self.request.user)

        def perform_create(self, serializer):
            serializer.save(user=self.request.user)

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = CartItem.objects.all()
        serializer_class = CartItemSerializer
        permission_classes = [permissions.IsAuthenticated]

        def get_queryset(self):
            return self.queryset.filter(user=self.request.user)