from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^about/', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/', TemplateView.as_view(template_name='contact.html')),
    url(r'^projects/', TemplateView.as_view(template_name='projects.html')),
    url(r'^blog/', TemplateView.as_view(template_name='blog.html')),

    url(r'^admin/', include(admin.site.urls)),
)
