# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url( r'^usep/admin/', include(admin.site.urls) ),  # eg host/project_x/admin/

    url( r'^usep/', include('usep_app.urls_app') ),  # eg host/project_x/anything/

)
