from rest_framework import serializers
from core.models import Kudos
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}" if obj.first_name and obj.last_name else obj.username

class KudosSerializer(serializers.ModelSerializer):
    giver = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Kudos
        fields = ["id", "giver", "receiver", "message", "timestamp"]