import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picasso_files.settings")
app = Celery("picasso_files")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()