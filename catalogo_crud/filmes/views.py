from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import FilmeForm
from .models import Filme
# Create your views here.

def criar_filme(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_filmes")
    else:
        form = FilmeForm()

    return render(
        request, "filme_form.html",
        {"form": form}
    )

def lista_filmes(request):
    filmes = Filme.objects.order_by(
        "assistido", "titulo"
    )
    return render(
        request, "lista.html",
        {"filmes": filmes}
    )

def detalhe_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    return render(
        request, "detalhe.html",
        {"filme": filme}
    )

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == "POST":
        form = FilmeForm(
            request.POST, instance=filme
        )
        if form.is_valid():
            form.save()
            return redirect(
                "detalhe_filme", pk=filme.pk
            )
    else:
        form = FilmeForm(instance=filme)

    return render(
        request, "filme_form.html",
        {"form": form, "filme": filme}
    )

def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == "POST":
        filme.delete()
        return redirect("lista_filmes")

    return render(
        request, "confirmar_exclusao.html",
        {"filme": filme}
    )

def definir_nome(request):
    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()

        if nome:
            request.session["nome_visitante"] = nome
            return redirect("lista_filmes")

    return render(request, "nome.html")

def lista_filmes(request):
    tema = request.session.get("tema", "dia")
    
    if tema == "dia":
        proximo_tema = "noite"
    else:
        proximo_tema = "dia"
    
    nome = request.session.get("nome_visitante", "Visitante")
    filmes = Filme.objects.order_by("titulo")

    return render(
        request, 
        "lista.html",
        {"filmes": filmes,
          "nome": nome,
          "tema": tema,
          "proximo_tema": proximo_tema,
        }
    )

def esquecer_nome(request):
    request.session.pop("nome_visitante", None)
    return redirect("lista_filmes")

@require_POST
def salvar_nome(request):
    nome = request.POST.get("nome", "").strip()[:40]
    if nome:
        request.session["nome_visitante"] = nome
    return redirect("lista_filmes")

@require_POST
def esquecer_nome(request):
    request.session.pop("nome_visitante", None)
    return redirect("lista_filmes")

def alternar_tema(request):
    tema_atual = request.session.get("tema", "dia")

    if tema_atual == "dia":
        request.session["tema"] = "noite"
    else:
        request.session["tema"] = "dia"

    return redirect("lista_filmes")