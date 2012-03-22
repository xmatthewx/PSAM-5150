# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',

#    url(r'^$', 'census.views.censushome', name='census_main'),
#    url(r'^census/$', 'census.views.sitecensus', name='site_census'),

    url(r'^$', 'census.views.censushome', name='census_main'),
    url(r'^census/$', 'census.views.sitecensus', name='site_census'),
    url(r'^results/$', 'census.views.censusresults', name='census_results'),
    url(r'^state_archive/$', 'census.views.statearchive', name='state_archive'),
    

)
