from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<novel_slug>[0-9 a-z -]+)/$', views.NovelView.as_view(), name='novel'),
    url(r'^(?P<novel_slug>[0-9 a-z -]+)/(?P<chapter_slug>[0-9 a-z -]+)/$', views.ChapterView.as_view(), name='chapter'),
]
