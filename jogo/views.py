# jogo/views.py
import random
from django.shortcuts import render

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
    return render(request, 'jogo/jogar.html', ctx)