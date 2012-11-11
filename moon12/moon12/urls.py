from coffin import shortcuts
from coffin.conf.urls.defaults import patterns, url
from django.http import HttpResponse
import jinja2

@jinja2.contextfunction
def get_context(c):
  if '_context' in c:
    return c['_context']
  return c

def render_to_response(template_file, context={}, request=None, mimetype="text/html"):
  context['context'] = get_context
  response = shortcuts.render_to_response(template_file, context)
  return HttpResponse(response, mimetype=mimetype)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'artful.views.root', name='root'),
    url(r'^opening$', 'artful.views.opening', name='opening'),
    url(r'^about', 'artful.views.about', name='about'),
    url(r'^events', 'artful.views.events', name='events'),
    url(r'^exhibits$', 'artful.views.exhibits', name='exhibits'),
    url(r'^artists$', 'artful.views.artists', name='artists'),
    url(r'^artist/([\w-]+)$', 'artful.views.artist', name='artist')

    # Examples:
    # url(r'^$', 'moon12.views.home', name='home'),
    # url(r'^moon12/', include('moon12.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
