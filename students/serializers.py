from rest_framework import serializers
from .models import Ride


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            'ride_id',
            'driver',
            'status',
            'fare',
            'created_at',
        ]