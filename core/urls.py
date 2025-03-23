from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.api.views.users import UserViewSet, OrganizationViewSet
from core.api.views.kudos import KudosAPIView
from core import views


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'organizations', OrganizationViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('kudos/', KudosAPIView.as_view(), name='kudos' ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

