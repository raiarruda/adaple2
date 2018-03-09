from django.shortcuts import render, redirect, render_to_response 
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext,loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import db_edp, db_edp_aluno, db_recursos
from .forms import form_edp, form_edp_aluno, form_add_recursos_edp
# Create your views here.

def inicio(request):
    edps = db_edp.objects.all()

    return render(request, 'core/inicio.html', {'title': 'Estruturas Digitais Pedagogicas','edps':edps})


def edp_nova(request):
    if request.method == "POST":
        form = form_edp(request.POST)
        if form.is_valid():
           
            edp = form.save(commit=False)
            edp.usuario = request.user
            edp.save()

            return redirect('inicio')
        else:
            return redirect('inicio')
    else:
        form = form_edp()
    return render( request, 'core/edp_nova.html', {'form':form})


def add_recurso_edp(request,pk):
    assert isinstance(request, HttpRequest)

    edp = db_edp.objects.all().get(pk=pk)

    if request.method == "POST":
        form = form_add_recursos_edp(request.POST)
        if form.is_valid():
            recursos = form.save(commit=False)
            recursos.edp = edp
            recursos.save()

            return redirect('inicio')
        else:
            return redirect('inicio')
    else:
        form = form_add_recursos_edp()
    return render( request, 'core/add_recurso_edp.html', {'form':form})


def visualizarEDP (request, pk):
    assert isinstance(request, HttpRequest)

    edp = db_edp.objects.all().get(pk=pk)
    habilidades = edp.habilidades
    
   # recursos = db_recursos.objects.all().get(edp=edp)
    recursos = db_recursos.objects.all().get(edp=edp)


    return render (request, 'core/visualizar.html', {'title': 'Visualizar EDP','edp': edp, 'recursos':recursos })



def responderEDP (request, pk):

    assert isinstance(request, HttpRequest)

    edp = db_edp.objects.all().get(pk=pk)

    #edp_aluno = db_edp_aluno.objects.create(aluno=request.user, edp=edp)
    if request.method == "POST":

        form = form_edp_aluno(request.POST)
        if form.is_valid():
            edp_aluno = form.save(commit=False)
            edp_aluno.aluno=request.user
            edp_aluno.edp=edp
            edp_aluno.save()

            return redirect('inicio')
        else:
           #para o botao cancela
            return redirect('inicio') 
    else:
        form = form_edp_aluno()

    return render (request, 'core/responder.html', {'title': 'Responder EDP', 'edp':edp, 'form':form})