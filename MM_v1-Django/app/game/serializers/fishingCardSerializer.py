from rest_framework import serializers
from dataset.models import FishingCard


class FishingCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FishingCard
        fields = '__all__'
