"""
Razorpay integration — disabled for personal/free setup.
All functions are no-ops that log a warning instead of hitting the API.
"""

import logging

logger = logging.getLogger(__name__)

_DISABLED_MSG = (
    "Razorpay is not configured in this personal setup. "
    "Payment payout functions will not run."
)


def authenticated_request(path, payload=None):
    logger.warning(_DISABLED_MSG)
    return None


def create_contact(account):
    logger.warning(_DISABLED_MSG)
    return None


def create_fund_account(account):
    logger.warning(_DISABLED_MSG)
    return None
