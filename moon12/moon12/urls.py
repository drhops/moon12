from coffin import shortcuts
from coffin.conf.urls.defaults import patterns, url
from django.conf.urls.defaults import include
from django.contrib import admin
from django.http import HttpResponse
import jinja2

admin.autodiscover()

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
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'artful.views.root', name='root'),
    url(r'^opening$', 'artful.views.opening', name='opening'),
    url(r'^gallery', 'artful.views.about', name='about'),
    url(r'^events', 'artful.views.events', name='events'),
    url(r'^exhibits$', 'artful.views.exhibits', name='exhibits'),
    url(r'^artists$', 'artful.views.artists', name='artists'),
    url(r'^artist/([\w-]+)/statement$', 'artful.views.artist_statement', name='artist_statement'),
    url(r'^artist/([\w-]+)/bio$', 'artful.views.artist_bio', name='artist_bio'),
    url(r'^artist/([\w-]+)/essays$', 'artful.views.artist_essays', name='artist_essays'),
    url(r'^artist/([\w-]+)/gallery$', 'artful.views.artist_gallery', name='artist_gallery'),
    url(r'^event/([\w-]+)/photos$', 'artful.views.event_photos', name='event_photos'),

    # Examples:
    # url(r'^$', 'moon12.views.home', name='home'),
    # url(r'^moon12/', include('moon12.foo.urls')),
)
