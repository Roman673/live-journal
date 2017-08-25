from django.conf.urls import url

from .views import (
    IndexView,
    TopicList,
    TopicDetail,
    TopicCreate,
    TopicUpdate,
    TopicDelete,
    EntryCreate,
    EntryDetail,
    EntryUpdate,
    EntryDelete,
)

app_name = 'learning_logs'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'), 
    url(r'^topics/$', TopicList.as_view(), name='topics'),
    url(r'^topic-add/$', TopicCreate.as_view(), name='topic_create'),
    url(r'^topic/(?P<slug>[\w-]+)/update/$', TopicUpdate.as_view(), name='topic_update'),
    url(r'^topic/(?P<slug>[\w-]+)/delete/$', TopicDelete.as_view(), name='topic_delete'),
    url(r'^topic/(?P<slug>[\w-]+)/$', TopicDetail.as_view(), name='topic'),
    url(r'^topic/(?P<slug>[\w-]+)/entry-add/$', EntryCreate.as_view(), name='entry_create'),
    url(r'^entry/(?P<slug>[\w-]+)/$', EntryDetail.as_view(), name='entry'),
    url(r'^entry/(?P<slug>[\w-]+)/update/$', EntryUpdate.as_view(), name='entry_update'),
    url(r'^entry/(?P<slug>[\w-]+)/delete/$', EntryDelete.as_view(), name='entry_delete'),
]
