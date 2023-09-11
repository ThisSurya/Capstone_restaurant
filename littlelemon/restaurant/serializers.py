from rest_framework.serializers import ModelSerializer
from . import models

class MenuSerializer(ModelSerializer):
    class Meta:
        model = models.Menu
        # fields = "__all__"
        fields = ["Title", "Price", "Inventory"]

class BookingSerializer(ModelSerializer):
    class Meta: 
        model = models.Booking
        fields = "__all__"