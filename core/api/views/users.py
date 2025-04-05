from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Organization
from core.serializers.users import UserSerializer, OrganizationSerializer
from rest_framework.views import APIView


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get_queryset(self):
        """
        Returns only users belonging to the same organization as the logged-in user.
        """
        user = self.request.user

        if hasattr(user, "organizationmembership"):
            org = user.organizationmembership.organization
            return User.objects.filter(organizationmembership__organization=org).exclude(id=user.id)

        return User.objects.none()
class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({ "username": user.username, "organization": user.organizationmembership.organization.name })
