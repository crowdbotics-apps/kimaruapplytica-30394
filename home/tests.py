import json
from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from rest_framework.test import force_authenticate
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from http import HTTPStatus
from home.api.v1.viewsets import AppViewSet, SubscriptionViewSet, PlanViewSet
from home.models import Plan, Subscription, App

# Group tests by model artifacts ie, Subscription, Plan, App
User = get_user_model()


class AppTest(TestCase):
    def setUp(self):
        sample_data = {
            "name": "Amazon",
            "type": "Web",
            "framework": "Django",
            "subscription": 1,
        }
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )
        self.app = App.objects.create(**sample_data)

    def test_get(self):
        request = self.factory.get(reverse("home:apps"))
        force_authenticate(request, user=self.user)
        response = AppViewSet.as_view({"get": "list"})(request)
        # Check if name is as expected
        self.assertEqual(response.data[0]["name"], "Amazon")
        # check for succesful response
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_create(self):
        data = json.dumps(
            {"name": "Amazon", "type": "Web", "framework": "Django", "subscription": 1}
        )
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse("home:apps"), data=data, content_type="application/json"
        )
        # Check for succesful post
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_url(self):
        # check for succesful URL resolving
        assert reverse("home:apps") == "/apps/"
        assert resolve("/apps/").view_name == "home:apps"


class PlanTest(TestCase):
    def setUp(self):
        sample_data = {"name": "standard", "description": "standard", "price": 20}
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )
        self.plan = Plan.objects.create(**sample_data)

    def test_create(self):
        data = json.dumps({"name": "standard", "description": "standard", "price": 20})
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse("home:plans"), data=data, content_type="application/json"
        )
        # Check for succesful post
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_get(self):
        request = self.factory.get(reverse("home:plans"))
        force_authenticate(request, user=self.user)
        response = PlanViewSet.as_view({"get": "list"})(request)
        # Check if name is as expected
        self.assertEqual(response.data[0]["name"], "standard")
        # check for succesful response
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_url(self):
        # check for succesful URL resolving
        assert reverse("home:plans") == "/plans/"
        assert resolve("/plans/").view_name == "home:plans"


class SubscriptionTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        sample_data = {"app": 1, "plan": 1, "user": 1}
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )
        self.subscription = Subscription.objects.create(**sample_data)

    def test_get(self):
        request = self.factory.get(reverse("home:subscriptions"))
        force_authenticate(request, user=self.user)
        response = SubscriptionViewSet.as_view({"get": "list"})(request)
        # Check if app is as expected
        self.assertEqual(response.data[0]["app"], "1")
        # check for succesful response
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_create(self):
        data = json.dumps({"app": 1, "plan": 1, "user": 1})
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse("home:subscriptions"), data=data, content_type="application/json"
        )
        # Check for succesful post
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_url(self):
        # check for succesful URL resolving
        assert reverse("home:subscriptions") == "/subscriptions/"
        assert resolve("/subscriptions/").view_name == "home:subscriptions"
