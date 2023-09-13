from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        pass
    def test_getall(self):
        item = Menu.objects.all()
        self.assertEqual(item, "cola : 3.99")