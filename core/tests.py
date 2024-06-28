from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CartItem

class CartTests(APITestCase):
        def setUp(self):
            self.user = User.objects.create_user(username='testuser', password='testpass')
            refresh = RefreshToken.for_user(self.user)
            self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))

        def test_add_to_cart(self):
            response = self.client.post('/api/cart/', {'product': 'item1', 'quantity': 1})
            self.assertEqual(response.status_code, 201)
        
        def test_view_cart(self):
            CartItem.objects.create(user=self.user, product='item1', quantity=1)
            response = self.client.get('/api/cart/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.data), 1)

        def test_remove_from_cart(self):
            item = CartItem.objects.create(user=self.user, product='item1', quantity=1)
            response = self.client.delete(f'/api/cart/{item.id}/')
            self.assertEqual(response.status_code, 204)
# Create your tests here.
