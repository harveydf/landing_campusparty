from django.conf.urls import patterns, url

from .views import LandingCreateView


urlpatterns = patterns('',
    url(regex=r'^$', view=LandingCreateView.as_view(), name='campus'),
)