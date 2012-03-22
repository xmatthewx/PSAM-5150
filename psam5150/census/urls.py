# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',

#    url(r'^$', 'census.views.censushome', name='census_main'),
#    url(r'^census/$', 'census.views.sitecensus', name='site_census'),

    url(r'^$', 'census.views.censushome', name='census_main'),
    url(r'^census/$', 'census.views.sitecensus', name='site_census'),

    
)
