from django.urls import path
from app2.views import *
app_name='something'
urlpatterns=[
    path ('abd/',abd,name='abd'),
    path('raina/',raina,name='raina'),
]
