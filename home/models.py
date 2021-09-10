from django.db import models
from django.contrib.auth import get_user_model
from .base_model import BaseModel

User = get_user_model()

framework_choices = [("Django", "Django"), ("React Native", "React Native")]

type_choices = [("Web", "web"), ("Mobile", "Mobile")]


class Plan(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField()

    def __str__(self) -> str:
        return self.name


class App(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=10, choices=type_choices, default="Web")
    framework = models.CharField(
        max_length=20, choices=framework_choices, default="Django"
    )
    domain_name = models.CharField(max_length=50, blank=True, null=True)
    screenshot = models.URLField(null=True, blank=True)
    subscription = models.IntegerField()
    user = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Subscription(BaseModel):
    user = models.IntegerField()
    plan = models.IntegerField()
    app = models.IntegerField()

    def __str__(self) -> str:
        return self.name
