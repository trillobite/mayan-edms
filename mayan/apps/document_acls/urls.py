from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns('document_acls.views',
    url(r'^list_for/document/(?P<document_id>\d+)/$', 'document_acl_list', (), 'document_acl_list'),
)
