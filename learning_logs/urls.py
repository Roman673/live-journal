from django.conf.urls import url

from .views import (IndexView, TagListView, TagCreateView,
                    EntryCreate, EntryDetail, EntryUpdate, EntryDelete,
                    EntryListView, EntryNewListView, EntryPopularListView,
                    EntryTagListView, CommentCreate, CommentUpdate, CommentDelete, )

app_name = 'learning_logs'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^entry/add/$', EntryCreate.as_view(), name='entry_create'),
    url(r'^tags/$', TagListView.as_view(), name='tags'),
    url(r'^tag/add/$', TagCreateView.as_view(), name='tag_create'),
    url(r'^tag/(?P<slug>[\w-]+)/$', EntryTagListView.as_view(), name='entry_tag'),
    url(r'^entry/list/newest/$', EntryNewListView.as_view(), name='entry_newest'),
    url(r'^entry/list/viewed/$', EntryPopularListView.as_view(), name='entry_viewed'),
    url(r'^entry/list/$', EntryListView.as_view(), name='entries'),
    url(r'^entry/(?P<slug>[\w-]+)/$', EntryDetail.as_view(), name='entry'),
    url(r'^entry/(?P<slug>[\w-]+)/update/$',
        EntryUpdate.as_view(), name='entry_update'),
    url(r'^entry/(?P<slug>[\w-]+)/delete/$',
        EntryDelete.as_view(), name='entry_delete'),
    url(r'^entry/(?P<slug>[\w-]+)/comment/add/$',
        CommentCreate.as_view(), name='comment_create'),
    url(r'^comment/(?P<pk>\d+)/update/$',
        CommentUpdate.as_view(), name='comment_update'),
    url(r'^comment/(?P<pk>\d+)/delete/$',
        CommentDelete.as_view(), name='comment_delete'),
]
