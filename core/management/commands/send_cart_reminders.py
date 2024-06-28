from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from core.models import CartItem

class Command(BaseCommand):
        help = 'Send cart reminders to users with items in their cart'

        def handle(self, *args, **kwargs):
            users = User.objects.all()
            for user in users:
                cart_items = CartItem.objects.filter(user=user)
                if cart_items.exists():
                    item_list = ', '.join([item.product for item in cart_items])
                    send_mail(
                        'Cart Reminder',
                        f'You have the following items in your cart: {item_list}',
                        'from@example.com',
                        [user.email],
                        fail_silently=False,
                    )
            self.stdout.write(self.style.SUCCESS('Successfully sent cart reminders'),)