from django.db.models.signals import post_save
from django.dispatch import receiver

from expense.models import AbstractPayoutAccount, UserPayoutAccount
from expense.rzpx import create_contact, create_fund_account


def create_payout_account(instance: AbstractPayoutAccount):
    contact_response = create_contact(instance)
    instance.vendor_party_id = contact_response["id"]
    response = create_fund_account(instance)
    instance.vendor_account_number = response["id"]
    instance.vendor_account_type = response["account_type"]
    instance.save()


@receiver(post_save, sender=UserPayoutAccount)
def on_user_payout_account_create(
    sender, instance: AbstractPayoutAccount, created, *args, **kwargs
):
    if created:
        create_payout_account(instance)
