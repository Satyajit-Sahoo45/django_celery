import os

from celery import Celery
from time import sleep
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryproject.settings')

app = Celery('celeryproject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'every-01-minutes':{
        'task':'celeryapp.tasks.mail_send',
        'schedule':crontab(minute='*/1')
    }
}