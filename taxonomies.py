from django.db.models import TextChoices
from django.utils import timezone


def now_date():
    return timezone.now().date()


def now_date_time():
    return timezone.now()


class PayoutAccountType(TextChoices):
    BANK_ACCOUNT = "Bank Account", "Bank Account"
    VIRTUAL_PAYMENT_ADDRESS = (
        "Virtual Payment Address",
        "Virtual Payment Address",
    )

    @classmethod
    def to_razorpay(cls, account_type: str) -> str:
        if account_type == PayoutAccountType.BANK_ACCOUNT:
            return "bank_account"
        if account_type == PayoutAccountType.VIRTUAL_PAYMENT_ADDRESS:
            return "vpa"


class RazorContactType(TextChoices):
    VENDOR = "vendor", "Vendor"
    CUSTOMER = "customer", "Customer"
    EMPLOYEE = "employee", "Employee"
    SELF = "self", "Self"


class MasterType(TextChoices):
    STACKS = "stacks", "Stacks"
    PETCUBES = "petcubes", "Petcubes"
