from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.contrib import admin
from frontend.views import ExampleCreate
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^example/success',TemplateView.as_view(template_name="frontend/success.html")),
    url(r'^example/', ExampleCreate.as_view()),
    url(r'', include('djcroco.urls')),

)
