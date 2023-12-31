from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = 'tienda'



from .views import (
    home,
	mensajes_privados,
	DetailMs,
	CanalDetailView,
	Inbox
	

)

UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

urlpatterns=[
	path('', views.home, name = 'home'),
	re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),
	path("dm/<str:username>", mensajes_privados),
	path("ms/<str:username>", DetailMs.as_view(), name="detailms"),
	path("inbox/", Inbox.as_view(), name="inbox"),
]