from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^$', 'scup.tournaments.views.index'),
    (r'^(?P<year>\d{4})/$', 'scup.tournaments.views.view_year'),
    (r'^(?P<year>\d{4})/(?P<slug>[\d\w\-]*)/$', 'scup.tournaments.views.view_event'),
)
