from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class BaseQueryset(QuerySet):
    """
    define custom queryset methods that can be chained for desired effect
    """

    def active_records(self) -> QuerySet:
        """
        :return:  A filtered queryset where the is_deleted flag is False
        """
        return self.filter(active=False)


class BaseManager(models.Manager):
    """
    override the get_queryset functions to return our custom queryset.
    """

    def get_queryset(self) -> BaseQueryset:
        """
        :return: custom queryset BaseQueryset
        """
        return BaseQueryset(self.model)


class BaseModel(models.Model):

    objects = BaseManager()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def soft_delete(self):

        self.active = False
        self.deleted_at = timezone.now()
        self.save()
