import django_filters

from ecommerce.models import (
    Customer,
    CustomerUser,
    Delivery,
    DeliveryAddress,
    DeliveryPartner,
    DispatchLine,
    ItemMaster,
    Order,
    OrderLine,
    PriceMatrix,
)
from finflow.models import Tenant


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    phone = django_filters.CharFilter(lookup_expr="icontains")
    tenant = django_filters.ModelChoiceFilter(queryset=Tenant.objects.all())

    class Meta:
        model = Customer
        fields = ["name", "email", "phone", "is_active", "tenant"]


class CustomerUserFilter(django_filters.FilterSet):
    customer = django_filters.ModelChoiceFilter(
        queryset=Customer.objects.all()
    )
    user_username = django_filters.CharFilter(
        field_name="user__username", lookup_expr="icontains"
    )
    user_email = django_filters.CharFilter(
        field_name="user__email", lookup_expr="icontains"
    )

    class Meta:
        model = CustomerUser
        fields = ["customer", "user", "user_username", "user_email"]


class DeliveryPartnerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    contact_email = django_filters.CharFilter(lookup_expr="icontains")
    contact_phone = django_filters.CharFilter(lookup_expr="icontains")
    tenant = django_filters.ModelChoiceFilter(queryset=Tenant.objects.all())

    class Meta:
        model = DeliveryPartner
        fields = [
            "name",
            "contact_email",
            "contact_phone",
            "is_active",
            "tenant",
        ]


class DeliveryAddressFilter(django_filters.FilterSet):
    customer = django_filters.ModelChoiceFilter(
        queryset=Customer.objects.all()
    )
    city = django_filters.CharFilter(lookup_expr="icontains")
    state = django_filters.CharFilter(lookup_expr="icontains")
    postal_code = django_filters.CharFilter(lookup_expr="icontains")
    country = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = DeliveryAddress
        fields = [
            "customer",
            "city",
            "state",
            "postal_code",
            "country",
            "is_active",
        ]


class ItemMasterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    netsuite_internal_id = django_filters.CharFilter(lookup_expr="icontains")
    tenant = django_filters.ModelChoiceFilter(queryset=Tenant.objects.all())

    class Meta:
        model = ItemMaster
        fields = ["name", "netsuite_internal_id", "active", "tenant"]


class PriceMatrixFilter(django_filters.FilterSet):
    item = django_filters.ModelChoiceFilter(queryset=ItemMaster.objects.all())
    min_quantity = django_filters.NumberFilter()
    max_quantity = django_filters.NumberFilter()
    price_per_unit = django_filters.NumberFilter()
    price_per_unit_min = django_filters.NumberFilter(
        field_name="price_per_unit", lookup_expr="gte"
    )
    price_per_unit_max = django_filters.NumberFilter(
        field_name="price_per_unit", lookup_expr="lte"
    )

    class Meta:
        model = PriceMatrix
        fields = [
            "item",
            "min_quantity",
            "max_quantity",
            "price_per_unit",
            "price_per_unit_min",
            "price_per_unit_max",
        ]


class OrderFilter(django_filters.FilterSet):
    customer = django_filters.ModelChoiceFilter(
        queryset=Customer.objects.all()
    )
    order_number = django_filters.CharFilter(lookup_expr="icontains")
    partner_purchase_order_number = django_filters.CharFilter(
        lookup_expr="icontains"
    )
    state = django_filters.CharFilter(lookup_expr="exact")
    tenant = django_filters.ModelChoiceFilter(queryset=Tenant.objects.all())
    created_by = django_filters.NumberFilter(field_name="created_by__id")
    request_delivery_date = django_filters.DateFilter()
    request_delivery_date_from = django_filters.DateFilter(
        field_name="request_delivery_date", lookup_expr="gte"
    )
    request_delivery_date_to = django_filters.DateFilter(
        field_name="request_delivery_date", lookup_expr="lte"
    )
    created_from = django_filters.DateTimeFilter(
        field_name="created", lookup_expr="gte"
    )
    created_to = django_filters.DateTimeFilter(
        field_name="created", lookup_expr="lte"
    )

    class Meta:
        model = Order
        fields = [
            "customer",
            "order_number",
            "partner_purchase_order_number",
            "state",
            "tenant",
            "created_by",
            "request_delivery_date",
            "request_delivery_date_from",
            "request_delivery_date_to",
            "created_from",
            "created_to",
        ]


class OrderLineFilter(django_filters.FilterSet):
    order = django_filters.ModelChoiceFilter(queryset=Order.objects.all())
    item = django_filters.ModelChoiceFilter(queryset=ItemMaster.objects.all())
    quantity = django_filters.NumberFilter()
    quantity_min = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="gte"
    )
    quantity_max = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="lte"
    )
    applied_price = django_filters.NumberFilter()
    applied_price_min = django_filters.NumberFilter(
        field_name="applied_price", lookup_expr="gte"
    )
    applied_price_max = django_filters.NumberFilter(
        field_name="applied_price", lookup_expr="lte"
    )

    class Meta:
        model = OrderLine
        fields = [
            "order",
            "item",
            "quantity",
            "quantity_min",
            "quantity_max",
            "applied_price",
            "applied_price_min",
            "applied_price_max",
        ]


class DeliveryFilter(django_filters.FilterSet):
    order = django_filters.ModelChoiceFilter(queryset=Order.objects.all())
    delivery_partner = django_filters.ModelChoiceFilter(
        queryset=DeliveryPartner.objects.all()
    )
    delivery_address = django_filters.ModelChoiceFilter(
        queryset=DeliveryAddress.objects.all()
    )
    dispatch_date = django_filters.DateFilter()
    dispatch_date_from = django_filters.DateFilter(
        field_name="dispatch_date", lookup_expr="gte"
    )
    dispatch_date_to = django_filters.DateFilter(
        field_name="dispatch_date", lookup_expr="lte"
    )
    tracking_information = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Delivery
        fields = [
            "order",
            "delivery_partner",
            "delivery_address",
            "dispatch_date",
            "dispatch_date_from",
            "dispatch_date_to",
            "tracking_information",
        ]


class DispatchLineFilter(django_filters.FilterSet):
    delivery = django_filters.ModelChoiceFilter(
        queryset=Delivery.objects.all()
    )
    order_line = django_filters.ModelChoiceFilter(
        queryset=OrderLine.objects.all()
    )
    quantity = django_filters.NumberFilter()
    quantity_min = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="gte"
    )
    quantity_max = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="lte"
    )

    class Meta:
        model = DispatchLine
        fields = [
            "delivery",
            "order_line",
            "quantity",
            "quantity_min",
            "quantity_max",
        ]
