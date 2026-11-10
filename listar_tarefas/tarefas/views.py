from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
from django.db.models import Case, When, Value, IntegerField
from django.contrib import messages

# Create your views here.
def lista_tarefas(request):
    status = request.GET.get('status', 'todas')
    busca = request.GET.get('busca', '') # Pega o termo da busca

    # 1. Começa com todas as tarefas
    tarefas = Tarefa.objects.all()

    # 2. Aplica o filtro de status
    if status == 'concluidas':
        tarefas = tarefas.filter(concluida=True)
    elif status == 'pendentes':
        tarefas = tarefas.filter(concluida=False)

    # 3. Aplica a busca por título (se o usuário digitou algo)
    if busca:
        tarefas = tarefas.filter(titulo__icontains=busca)

    # 4. Aplica a ordenação por prioridade (que já fizemos)
    ordenacao_prioridade = Case(
        When(prioridade='alta', then=Value(1)),
        When(prioridade='media', then=Value(2)),
        When(prioridade='baixa', then=Value(3)),
        output_field=IntegerField(),
    )
    tarefas = tarefas.order_by(ordenacao_prioridade)

    total_pendentes = Tarefa.objects.filter(concluida=False).count()
    total_concluidas = Tarefa.objects.filter(concluida=True).count()

    contexto = {
        'tarefas': tarefas,
        'titulo_pagina': 'Lista de Tarefas',
        'total_concluidas': total_concluidas,
        'total_pendentes': total_pendentes,
        'busca': busca # Enviamos de volta para o HTML para manter o texto na caixinha
    }
    return render(request, 'lista.html', contexto)


# STUBS 
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
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
            messages.success(request, 'Tarefa editada com sucesso!')
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
        messages.success(request, 'Status da tarefa alternado com sucesso!')
        return redirect('detalhe_tarefa', pk=tarefa.pk)
    
    else:
        return redirect('lista_tarefas')

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.warning(request, 'Tarefa excluida com sucesso!')
        return redirect('lista_tarefas')
    else:
        return render(request, 'excluir.html', {'tarefa': tarefa})