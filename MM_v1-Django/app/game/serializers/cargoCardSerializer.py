from rest_framework import serializers
from dataset.models import CargoCard


class CargoCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CargoCard
        fields = '__all__'
        # exclude = ['id']
