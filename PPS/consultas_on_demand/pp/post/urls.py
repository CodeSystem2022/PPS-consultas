from django.urls import re_path
from .views import inicio

app_name = 'post'
from .views import (
    inicio
)

urlpatterns = [
    re_path(r'^post_id/$', inicio, name='inicio')
]
