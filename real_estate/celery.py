from __future__ import absolute_import
import os

from celery import celery

from real_estate.settings import base

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "real_estate.settings.development")

app = Celery("real_estate")


app.config_from_object("real_estate.settings.development",
namespace = "CELERY")

app.autodiscover(lambda: base.INSTALLED_APPS)
