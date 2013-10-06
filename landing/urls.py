from django.conf.urls import patterns, url

from .views import LandingCreateView, ScenarioTemplateView


urlpatterns = patterns('',
    url(regex=r'^$', view=LandingCreateView.as_view(), name='campus'),
    url(regex=r'^speakers/(?P<scenario>[\w\-]+)/$', view=ScenarioTemplateView.as_view(), name='speakers'),
)
