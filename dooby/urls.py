from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dooby.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', 'blog.views.blog' , name='hello'),
    url(r'^acc/login/$','dooby.views.login'),
    url(r'^acc/auth/$','credento.views.auth_view'),
    url(r'^acc/loggedin/$','credento.views.loggedin'),
    url(r'^acc/invalid/$','credento.views.invalid_login'),
    url(r'^acc/logout/$','credento.views.logout'),
    url(r'^acc/register/$','credento.views.register_user'),
    url(r'^acc/register_true/$','credento.register_true'),
    url(r'^admin/', include(admin.site.urls)),
)
