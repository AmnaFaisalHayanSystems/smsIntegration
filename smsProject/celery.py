from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smsProject.settings')
app = Celery('smsProject')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     "fetch_latest_news_data": {
#         "task": "news.tasks.fetch_latest_news_data",
#         "schedule": crontab(minute="0"),
#     },
#     "fetch_tweets_against_tags": {
#         'task': "miscellaneous.tasks.fetch_tweets_against_tags",
#         "schedule": crontab(minute="0")
#     }
# }


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


