from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Car_shop.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^cart/$', 'order.views.cart'),
                       url(r'^cart_all/$', 'order.views.add_cart'),
                       url(r'^cart/(?P<id_cart>\d+)/$', 'order.views.delete_cart'),
)