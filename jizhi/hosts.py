from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host('www', settings.ROOT_URLCONF, name='www'),  # name与DEFAULT_HOST 相同
    host('web', 'edu_web.urls', name='web'),
    host('app', 'edu_app.urls', name='app'),
)