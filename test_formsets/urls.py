from django.conf.urls import patterns, include, url
from django.views import generic
from django.contrib import admin

from test_formsets import views

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.TestView.as_view()),
    # Examples:
    # url(r'^$', 'test_formsets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
