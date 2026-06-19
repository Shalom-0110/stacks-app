from django.contrib.auth.models import User
from django.db.models import F, QuerySet
from loguru import logger
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from finflow.models import ProjectAccess


class SerializedRelationField(serializers.Field):
    def __init__(
        self, lookup_key: str, queryset: QuerySet, repr_serializer, **kwargs
    ):
        self.lookup_key = lookup_key
        self.queryset = queryset
        self.repr_serializer = repr_serializer
        super(SerializedRelationField, self).__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            key = self.lookup_key.split("__")[-1]
            value = data[key] if isinstance(data, dict) else data
            logger.debug(
                f"Looking up {self.queryset.model.__name__} "
                f"with {self.lookup_key}: {value}"
            )
            return self.queryset.get(**{self.lookup_key: value})
            # logger.debug(f"Found ActivityBudget: {result}")
        except Exception as exc:
            logger.exception(f"Error in SerializedRelationField: {exc}")
            raise ValidationError(exc)

    def to_representation(self, value):
        return self.repr_serializer(instance=value, context=self.context).data


class LiteUserSerializer(ModelSerializer):
    full_name = serializers.CharField(source="get_full_name")
    picture = serializers.ImageField(source="usermetadata.picture")
    project_capabilities = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "full_name",
            "picture",
            "project_capabilities",
        )

    def get_project_capabilities(self, obj: User) -> dict:
        return {
            x.pop("slug"): x
            for x in ProjectAccess.objects.filter(user=obj)
            .annotate(slug=F("project__slug"))
            .values("slug")
            .annotate(
                approve_budget=F("can_approve_budget"),
                approve_finance=F("can_approve_finance"),
                modify_access=F("can_modify_access"),
                expense_access=F("can_create_expense"),
                approve_review_sheet=F("can_approve_review_sheet"),
            )
        }
