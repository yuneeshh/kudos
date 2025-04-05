from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.models import Kudos
from core.serializers.kudos import KudosSerializer

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        kudos_given = Kudos.objects.filter(giver=user)
        kudos_received = Kudos.objects.filter(receiver=user)
        kudos_left = 3 - kudos_given.count()  # Assuming 3 kudos per week

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "organization": user.organizationmembership.organization.name if hasattr(user, "organizationmembership") else "No Organization",
            },
            "kudos_left": max(0, kudos_left),
            "kudos_given": KudosSerializer(kudos_given, many=True).data,
            "kudos_received": KudosSerializer(kudos_received, many=True).data,
        })
