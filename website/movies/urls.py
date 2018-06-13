from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$',views.movies,name='movies'),
	url(r'^list/$',views.list.as_view(),name='list'),
	url(r'^(?P<pk>[0-9]+)/$',views.detail,name="detail")
]