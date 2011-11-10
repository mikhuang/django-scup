from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'tournaments.views.index'),
    (r'^tournament/(?P<id>\d+)/$', 'tournaments.views.view_event_by_id'),
    (r'^(?P<year>\d{4})/$', 'tournaments.views.view_year'),
    (r'^(?P<year>\d{4})/(?P<slug>[\d\w\-]*)/$', 'tournaments.views.view_event'),
)
