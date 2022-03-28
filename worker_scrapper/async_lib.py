

from celery import Celery

QUEUE_NAME = '_articles_to_scrap'


def scrap_article_async(article_title: str):

    celery_client = Celery('scrapper_client')
    celery_client.config_from_object('django.conf:settings')

    celery_client.send_task(
        name='worker_scrapper.tasks.scrap_article',
        kwargs={
            'article_title': article_title,
        },
        queue=QUEUE_NAME
    )