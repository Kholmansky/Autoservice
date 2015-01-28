__author__ = 'ads18'
from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Car_shop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^add/', 'checkup.views.add_checkup'),
                       url(r'^delete/(?P<id_service>\d+)/$', 'checkup.views.delete_checkup')
                        )