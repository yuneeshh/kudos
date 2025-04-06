from rest_framework import serializers
from django.contrib.auth.models import User
from core.services.kudo_service import KudoService


class GiveKudosValidator(serializers.Serializer):
    receiver_id = serializers.IntegerField()
    message = serializers.CharField(max_length=280, required=False, allow_blank=True)

    def validate_receiver_id(self, value):
        request_user = self.context["request"].user

        try:
            receiver = User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Receiver not found.")

        if request_user == receiver:
            raise serializers.ValidationError("You cannot give kudos to yourself.")

        if not hasattr(request_user, "organizationmembership"):
            raise serializers.ValidationError("You are not in an organization")

        if request_user.organizationmembership.organization != receiver.organizationmembership.organization:
            raise serializers.ValidationError("You can only give kudos within your organization.")

        if not KudoService.can_give_kudos(request_user):
            raise serializers.ValidationError("You have reached your kudos limit for this week.")

        return receiver
