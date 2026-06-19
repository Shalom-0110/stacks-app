"""
Celery tasks — personal/free setup.
NetSuite sync is disabled; tasks run synchronously (no Redis required)
because CELERY_TASK_ALWAYS_EAGER=True is set in settings.py.
"""

import logging

from stacks.celery import app

logger = logging.getLogger(__name__)


@app.task
def refresh_masters():
    """NetSuite master sync — no-op in personal setup."""
    logger.info(
        "refresh_masters: NetSuite integration is disabled. Nothing to sync."
    )
