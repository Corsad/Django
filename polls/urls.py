# from django.conf.urls import patterns, url
#
# from polls import views
#
# urlpatterns = patterns('',
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^specifics(?P<poll_id>\d+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
# )

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
