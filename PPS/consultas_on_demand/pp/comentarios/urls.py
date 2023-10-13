from django.urls import re_path
from .views import post_idd, comentario_id, eliminarComentarios


app_name = 'comentarios'
urlpatterns = [
    re_path(r'^post_id/(?P<pk>\d+)/$', post_idd, name="post_idd"),
    re_path(r'^comentario_id/(?P<pk>\d+)/$', comentario_id, name="comentario_id"),
    re_path(r'^eliminar/(?P<id>\d+)/$', eliminarComentarios, name="eliminar"),
]
