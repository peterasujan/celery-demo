from __future__ import absolute_import
import os
from celery import Celery

_RABBIT = 'localhost'
if 'RABBIT_SERVER' in os.environ:
    _RABBIT = os.environ['RABBIT_SERVER']
_BROKER = 'amqp://guest:guest@{}//'.format(_RABBIT)

app = Celery('test_celery',
             broker=_BROKER,
             backend='rpc://',
             include=['test_celery.tasks'])
