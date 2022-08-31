from django.urls import re_path

from employer_admin import consumers

websocket_urlpatterns = [
    re_path(r'^ws/e_admin/product_admin/orders/$', consumers.PracticeConsumer.as_asgi()),
]