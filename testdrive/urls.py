__author__ = 'ads18'
from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Car_shop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^write/', 'testdrive.views.add_test_drive'),
                       url(r'^delete/(?P<id_service>\d+)', 'testdrive.views.delete_test_drive'),
                        )