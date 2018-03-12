#views app perfil

from django.conf.urls import include, url
import django.contrib.auth.views

from . import views


from datetime import datetime
urlpatterns = [
    url(r'^todosalunos/', views.listaralunos, name='listaralunos'),
    url(r'^aluno/(?P<pk>[0-9]+)/$', views.perfilaluno, name='perfilaluno'),
   # url(r'^aluno/edp/(?P<pk2>[0-9]+)/',views.resposta_edp_aluno,name='aluno_ver_edp'),

    
]