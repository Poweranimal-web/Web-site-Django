from django.urls import re_path
from django.urls import path

from employer_admin import consumers

websocket_urlpatterns = [
    re_path('ws/e_admin/product_admin/orders/', consumers.PracticeConsumer.as_asgi()),
]