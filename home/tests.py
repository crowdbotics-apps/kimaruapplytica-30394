import json
from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from http import HTTPStatus

# Create your tests here.
User = get_user_model()


class AppTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )

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
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )
        
    def test_create(self):
        data = json.dumps({"name": "standard", "description": "standard", "price": 20})
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            reverse("home:plans"), data=data, content_type="application/json"
        )
        # Check for succesful post
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_url(self):
        # check for succesful URL resolving
        assert reverse("home:plans") == "/plans/"
        assert resolve("/plans/").view_name == "home:plans"


class SubscriptionTest(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username="ironman", password="demo123123", email="iron@test.com"
        )

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
