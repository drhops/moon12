from coffin import shortcuts
from coffin.conf.urls.defaults import patterns, url
from django.http import HttpResponse
from django.template import RequestContext

def render_to_string(template, context, request=None):
    if request:
        context_instance = RequestContext(request)
    else:
        context_instance = None
    return shortcuts.render_to_string(template, context, context_instance)

def render_to_response(template, context={}, request=None, mimetype="text/html"):
    response = render_to_string(template, context, request)
    return HttpResponse(response, mimetype=mimetype)
  
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'artful.views.root', name='root'),
    url(r'^opening$', 'artful.views.opening', name='opening'),
    url(r'^artist/([\w-]+)$', 'artful.views.artist', name='artist')

    # Examples:
    # url(r'^$', 'moon12.views.home', name='home'),
    # url(r'^moon12/', include('moon12.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
