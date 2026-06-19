from django.contrib.auth.models import User
from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    FloatField,
    ForeignKey,
    IntegerField,
    JSONField,
    Model,
    TextField,
)
from django_countries.fields import CountryField

from expense.taxonomies import PayoutAccountType, RazorContactType


class AbstractPayoutAccount(Model):
    vendor = CharField(max_length=64, default="RazorpayX")
    vendor_account_number = CharField(max_length=128)
    vendor_account_type = CharField(max_length=64)
    vendor_party_id = CharField(max_length=64)
    account_type = CharField(max_length=64, choices=PayoutAccountType.choices)
    account_number = CharField(max_length=128)
    account_name = CharField(max_length=255)
    financial_institution_code = CharField(
        max_length=128, help_text="For example, IFSC for India"
    )
    is_active = BooleanField(default=True)

    class Meta:
        abstract = True
        unique_together = (("vendor_account_type", "vendor_account_number"),)

    @property
    def target_object(self):
        raise NotImplementedError

    @property
    def target_name(self):
        raise NotImplementedError

    @property
    def target_phone(self):
        raise NotImplementedError

    @property
    def target_razorpay_type(self):
        raise NotImplementedError


class UserPayoutAccount(AbstractPayoutAccount):
    user = ForeignKey(User, on_delete=PROTECT)
    razorpay_contact_type = CharField(
        max_length=32,
        choices=RazorContactType.choices,
        default=RazorContactType.EMPLOYEE,
    )

    def __str__(self):
        return (
            f"{self.user} / {self.vendor_account_type} / "
            f"{self.vendor_account_number}"
        )

    @property
    def target_object(self):
        return self.user

    @property
    def target_name(self):
        return self.user.get_full_name() or self.user.email

    @property
    def target_razorpay_type(self):
        return RazorContactType.SELF

    @property
    def target_phone(self):
        return self.user.userprofile.phone


class AbstractAddress(Model):
    address_line = TextField(blank=True)
    latitude = FloatField(blank=True, null=True)
    longitude = FloatField(blank=True, null=True)
    postal_code = IntegerField(blank=True, null=True)
    city = CharField(max_length=255, blank=True)
    state = CharField(max_length=255, blank=True)
    country = CharField(
        max_length=2, choices=list(CountryField().choices), default="IN"
    )
    places_api_json = JSONField(default=dict, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.address_line} / {self.postal_code}"

    @property
    def country_display(self):
        return self.get_country_display()

    @property
    def state_short_name(self):
        address = self.places_api_json.get("address_component", [])
        for entry in address:
            types = entry.get("types", [])
            if "administrative_area_level_1" not in types:
                continue
            return entry.get("short_name", "")
        return ""

    @property
    def is_india_union_territory(self):
        union_territories = ["AN", "CH", "DH", "DL", "JK", "LA", "LD", "PY"]
        return (
            True
            if self.state_short_name in union_territories
            and self.country == "IN"
            else False
        )
