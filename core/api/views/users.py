from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from core.models import Organization
from core.serializers.users import UserSerializer, OrganizationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

