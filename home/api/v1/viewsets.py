from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    AppSerializer,
    PlanSerializer,
    SubscriptionSerializer,
)
from home.models import App, Plan, Subscription


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})

# all views require basic auth
class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    lookup_field = "id"
    premission_classes = [IsAuthenticated]
    # ensure a user only sees apps registered under their user account
    def get_queryset(self):
        user = self.request.user
        return App.objects.filter(user=user.id)
    


class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    lookup_field = "id"
    http_method_names = ["get", "head"]
    premission_classes = [IsAuthenticated]


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    lookup_field = "id"
    http_method_names = ["get", "post", "head", "put", "patch"]
    premission_classes = [IsAuthenticated]
