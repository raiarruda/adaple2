from django.conf.urls import include, url
import django.contrib.auth.views
from . import forms
from . import views


from datetime import datetime
urlpatterns = [
    url(r'^inicio', views.inicio, name='inicio'),
    url(r'^edp/(?P<pk>[0-9]+)/$', views.visualizarEDP, name='edp'),
    url(r'^edp/(?P<pk>[0-9]+)/adiciona_recursos$', views.add_recurso_edp, name='add_recurso_edp'),
    url(r'^edp/(?P<pk>[0-9]+)/responder$', views.responderEDP, name='edp_responder'),
    url(r'^edp/nova/$', views.edp_nova, name='edp_nova'),
    url(r'^$',
        django.contrib.auth.views.login,
        {
            'template_name': 'core/login.html',
            'authentication_form': forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Entrar',
                'year': datetime.now().year,
            },
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
#    url(r'^chat', views.chat, name='chat'),
#    url(r'^temas', app.views.temas, name='temas'),
#    url(r'^titulo', app.views.titulo, name='titulo'),
#    url(r'^aguardo', app.views.aguardo, name='aguardo'),
#    url(r'^escrita', app.views.escrita, name='escrita'),
]