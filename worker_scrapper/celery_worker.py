from celery import Celery
from worker_scrapper.async_lib import QUEUE_NAME


# create the worker connected only with its tasks file
worker_scrapper = Celery('worker_scrapper', include=['worker_scrapper.tasks'])

worker_scrapper.select_queues([QUEUE_NAME])


# configure the worker based on the settings that start with
# the namespace prefix parameter
worker_scrapper.config_from_object('django.conf:settings')