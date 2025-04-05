from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Kudos
from core.serializers.kudos import KudosSerializer
from core.api.validators import GiveKudosValidator
from core.services.kudo_service import KudoService


class KudosAPIView(APIView):

    def get(self, request):
        """Retrieve kudos given and received by the authenticated user."""
        user = request.user
        given_kudos = Kudos.objects.filter(giver=user).select_related('giver', 'receiver')
        received_kudos = Kudos.objects.filter(receiver=user).select_related('giver', 'receiver')

        return Response({
            "given": KudosSerializer(given_kudos, many=True).data,
            "received": KudosSerializer(received_kudos, many=True).data
        }, status=status.HTTP_200_OK)

    def post(self, request):
        """Give a kudo to another user."""
        validator = GiveKudosValidator(data=request.data, context={"request": request})
        validator.is_valid(raise_exception=True)

        giver = request.user
        receiver = validator.validated_data["receiver_id"]
        message = validator.validated_data.get("message", "")

        kudo = KudoService.give_kudos(giver, receiver, message)
        return Response(KudosSerializer(kudo).data, status=status.HTTP_201_CREATED)

