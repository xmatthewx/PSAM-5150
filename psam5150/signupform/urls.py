# -*- coding: UTF-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'signupform.views.signuphome', name='signup_main'),
    url(r'^helloworld/$', 'signupform.views.helloworld', name='hello_world'),
    #url(r'^hellocontact/$', 'signupform.views.hellocontact', name='hello_contact'),
    url(r'^sign_up/$', 'signupform.views.sitesignup', name='site_signup'),
    url(r'^contact/$', 'signupform.views.sitecontact', name='site_contact'),
    url(r'^hello$', 'signupform.views.hello', name='hello'),
)
