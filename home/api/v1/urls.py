from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    AppViewSet,
    PlanViewSet,
    SubscriptionViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("apps", AppViewSet, basename="apps")
router.register("plans", PlanViewSet, basename="plans")
router.register("subscription", SubscriptionViewSet, basename="subscription")

urlpatterns = [
    path("", include(router.urls)),
]
