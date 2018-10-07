from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
    LikeToggleAPIView,
    RetweetAPIView,
    TweetCreateAPIView,
    TweetListAPIView,
    TweetDetailAPIView,
    ) 

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")),  # /tweets/
    url(r'^$', TweetListAPIView.as_view(), name='list'),  # /api/tweets/
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),  # /tweets/create/
    url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name='detail'),  # /api/tweets/id/retweet/
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),  # /api/tweets/id/retweet/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),  # /api/tweets/id/retweet/
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),  # /tweets/1/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),  # /tweets/1/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),  # /tweets/1/delete/
]

