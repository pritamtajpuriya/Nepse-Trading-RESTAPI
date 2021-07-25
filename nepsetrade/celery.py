

#  setting the default Django settings module for the ‘celery’ 


import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nepsetrade.settings')
 
app = Celery('nepsetrade')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
