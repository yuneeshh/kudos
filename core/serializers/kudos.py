from rest_framework import serializers
from core.models import Kudos

class KudosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kudos
        fields = ["id", "giver", "receiver", "timestamp"]
        read_only_fields = ["id", "giver", "timestamp"]
