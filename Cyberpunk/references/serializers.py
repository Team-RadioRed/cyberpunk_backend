from rest_framework import serializers
from .models import Weapon


class WeaponListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name_rus']  # поля для списка оружия


class WeaponDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'  # все поля для деталей конкретного оружия
