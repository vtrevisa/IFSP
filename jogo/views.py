# jogo/views.py
import random
from django.shortcuts import render
from .models import Partida

# Create your views here.
def boas_vindas(request):
    return render( request, 'jogo/boas_vindas.html')

def jogar(request):
    OPCOES = ['pedra', 'papel', 'tesoura']

    jogada_usuario = request.GET.get('jogada', None)
    ctx = {'jogada_usuario': jogada_usuario}
    if jogada_usuario in OPCOES:
        jogada_pc = random.choice(OPCOES)
        ctx['jogada_pc'] = jogada_pc
        if jogada_usuario == jogada_pc:
            resultado = 'empate'
        elif (
            (jogada_usuario=='pedra' and jogada_pc=='tesoura') or
            (jogada_usuario=='papel' and jogada_pc=='pedra') or
            (jogada_usuario=='tesoura' and jogada_pc=='papel')
        ):
            resultado = 'vitoria'
        else:
            resultado = 'derrota'
        ctx['resultado'] = resultado

        Partida.objects.create(
            jogador=jogada_usuario,
            computador=jogada_pc,
            resultado=resultado,
        )
    
    return render(request, 'jogo/jogar.html', ctx)

def historico(request):
    partidas = Partida.objects.all()

    # Ordenando e Limitando
    partidas = (
        Partida.objects.order_by("-criada_em"))

    """ # Filtrando resultados
    partidas = (Partida.objects.filter(
        resultado = 'vitoria')
        [:4]
    ) """

    """ # Filtrando e ordenando resultados
    partidas = (Partida.objects.filter(
        resultado = 'vitoria').order_by("-criada_em")
        [:4]
    ) """

    # Contando resultados
    total = Partida.objects.all().count()
    vitorias = Partida.objects.filter(resultado = 'vitoria').count()
    derrotas = Partida.objects.filter(resultado = 'derrota').count()
    empates = Partida.objects.filter(resultado = 'empate').count()
    pedras = Partida.objects.filter(jogador = 'pedra').count()
    papeis = Partida.objects.filter(jogador = 'papel').count()
    tesouras = Partida.objects.filter(jogador = 'tesoura').count()
    

    """ # Retornando colunas específicas
    partidas = Partida.objects.values_list(
    "   jogador", "computador", "resultado"
    ) """

    
    return render(
        request,
        "jogo/historico.html",
        {
            "partidas": partidas, 
            "total": total,
            "vitorias": vitorias,
            "derrotas": derrotas,
            "empates": empates,
            "pedras": pedras,
            "papeis": papeis,
            "tesouras": tesouras
        }
    )