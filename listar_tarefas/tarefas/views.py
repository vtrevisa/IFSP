from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def lista_tarefas(request):
    status = request.GET.get('status', 'todas')
    
    if status == 'concluidas':
        tarefas = Tarefa.objects.filter(concluida=True)
    elif status == 'pendentes':
        tarefas = Tarefa.objects.filter(concluida=False)
    else:
        tarefas = Tarefa.objects.all()

    contexto = {
                'tarefas': tarefas,
                'titulo_pagina': 'Lista de Tarefas'
            }

    return render(request, 'lista.html', contexto)


# STUBS 
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    contexto = {
        'form': form,
        'titulo_formulario': 'Nova Tarefa'
    }

    return render(request, 'formulario.html', contexto)

def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    contexto = {
        'tarefa': tarefa
    }

    return render(request, 'detalhe.html', contexto)

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if tarefa and request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('detalhe_tarefa', pk=tarefa.pk)
    else:
        form = TarefaForm(instance=tarefa)
        
    contexto = {
        'tarefa': tarefa,
        'form': form,
        'titulo_formulario': 'Editar Tarefa'
    }

    return render(request, 'formulario.html', contexto)

def alternar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)

    if request.method == 'POST':
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
        return redirect('detalhe_tarefa', pk=tarefa.pk)
    
    else:
        return redirect('lista_tarefas')

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    else:
        return render(request, 'excluir.html', {'tarefa': tarefa})