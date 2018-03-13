# views perfil.

from django.shortcuts import render, redirect, render_to_response 
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext,loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from projeto.core.models import db_edp, db_edp_aluno
# Create your views here.

def listaralunos(request):
   
    alunos = User.objects.filter(groups__name__in=['aluno'])
   
    return render(request, 'perfil/alunos.html', {'title': 'Alunos','alunos':alunos})


def perfilaluno(request,pk):
    aluno_perfil = User.objects.all().get(pk=pk)
    edps= db_edp_aluno.objects.all()
    edps_do_aluno = edps.filter(aluno=aluno_perfil)

    return render(request, 'perfil/visualizarperfil.html', {'title': 'Aluno','alunos':aluno_perfil,'edps':edps_do_aluno})

def resposta_edp_aluno(request,pk):
    edp_aluno = db_edp_aluno.objects.all().get(pk=pk)
    edp = edp_aluno.edp
    teste = "testeeeee"
    return render(request, 'perfil/visualizar_aluno_edp.html', {'title': 'Visualizar EDP','edp':edp, 'teste':teste})
    
