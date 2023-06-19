import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EatTop.settings")
app = Celery("EatTop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.control.purge()
app.autodiscover_tasks()
