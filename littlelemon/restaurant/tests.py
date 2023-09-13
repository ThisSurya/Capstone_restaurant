from django.test import TestCase
from restaurant.models import Menu
from .serializers import MenuSerializer


class MenuTest(TestCase):
    
    def test_get_down(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')

class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="Eskrim", price=14, inventory=75)
    def test_getall(self):
        item = Menu.objects.all()
        serialized_item = MenuSerializer(item, many=True)
        
