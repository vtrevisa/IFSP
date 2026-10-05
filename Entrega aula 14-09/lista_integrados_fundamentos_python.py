import datetime, subprocess, os

'''
Parte 1 — Estruturas de Decisão e Repetição
Exercício 1 — Classificador de faixa etária
Escreva um programa que leia a idade de uma pessoa e classifique em: criança (0-12),
adolescente (13-17), adulto (18-59) ou idoso (60+). Utilize apenas estruturas de decisão
(if/elif/else).
'''

def lifp01():
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade < 0:
        print("Idade inválida.")
    elif idade <= 12:
        print("Classificação: Criança")
    elif idade <= 17:
        print("Classificação: Adolescente")
    elif idade <= 59:
        print("Classificação: Adulto")
    else:
        print("Classificação: Idoso")

'''
Exercício 2 — Validação de formulário de cadastro
Peça ao usuário nome, idade e e-mail. Valide: nome não pode ser vazio, idade deve ser
um número entre 0 e 120, e-mail deve conter '@' e um '.' após o '@'. Se algum campo
for inválido, informe qual e peça novamente, usando um laço while até que todos os
dados sejam válidos
'''

def lifp02():
    while True:
        nome = input("Digite o nome: ")
        idade_str = input("Digite a idade: ")
        email = input("Digite o e-mail: ")

        erros = []

        # Validação Nome (não pode ser vazio)
        if not nome:
            erros.append("O nome não pode ser vazio.")
            
        # Validação da Idade (deve ser número entre 0 e 120)
        if not idade_str.isdigit():
            erros.append("A idade deve ser um número inteiro válido.")
        else:
            idade = int(idade_str)
            if idade < 0 or idade > 120:
                erros.append("A idade deve estar entre 0 e 120 anos.")
                
        # Validação do E-mail (deve conter '@' e '.' após o '@')
        if '@' not in email:
            erros.append("O e-mail deve conter o caractere '@'.")
        else:
            # Divide o e-mail no primeiro '@' encontrado para checar o que vem depois
            usuario, dominio = email.split('@', 1)
            if '.' not in dominio:
                erros.append("O e-mail deve conter um ponto (.) após o '@'.")

        # Verifica validações
        if not erros:
            print("\n🎉 Cadastro realizado com sucesso!")
            print(f"Nome: {nome} | Idade: {idade_str} | E-mail: {email}")
            break  # Sai do laço pois todos os dados são válidos
        else:
            print("\n❌ Erro no cadastro! Corrija os seguintes problemas:")
            for erro in erros:
                print(f"- {erro}")
            print("Por favor, tente preencher todos os dados novamente.\n" + "-"*30)

            print("Cadastro realizado com sucesso!")
            break

'''
Exercício 3 — Remoção de duplicados e interseção de conjuntos
Dadas duas listas de e-mails cadastrados em sistemas diferentes, use conjuntos (set)
para: encontrar os e-mails que aparecem nos dois sistemas (interseção), os que
aparecem em apenas um deles (diferença simétrica) e a lista unificada sem duplicados
(união).
'''

def lifp03():
    sistema_a = [
    "ana.silva@email.com", "bruno.costa@email.com", "carlos.souza@email.com",
    "diego.lima@email.com", "ana.silva@email.com", "fernanda.melo@email.com"
    ]

    sistema_b = [
        "carlos.souza@email.com", "diego.lima@email.com", "gabriel.alves@email.com",
        "helena.santos@email.com", "gabriel.alves@email.com", "igor.oliveira@email.com"
    ]

    set_a = set(sistema_a)
    set_b = set(sistema_b)

    # Interseção: e-mails que aparecem nos dois sistemas
    intersecao = set_a & set_b

    # Diferença simétrica: e-mails que aparecem em apenas um dos sistemas
    diferenca_simetrica = set_a ^ set_b

    # União: lista unificada sem duplicados
    uniao = set_a | set_b

    # Convertendo a união para uma lista
    lista_unificada = list(uniao)

    # Exibindo os resultados
    print("E-mails nos dois sistemas (Interseção):")
    print(intersecao)

    print("\nE-mails em apenas um dos sistemas (Diferença Simétrica):")
    print(diferenca_simetrica)

    print("\nLista unificada sem duplicados (União):")
    print(lista_unificada)


'''
Exercício 4 — Agenda de contatos com tuplas e dicionário
Implemente uma agenda onde cada contato é uma tupla (nome, telefone, categoria),
armazenada em um dicionário cuja chave é a categoria (ex.: 'família', 'trabalho') e o 
valor é uma lista de tuplas (contatos). Escreva uma função que retorne todos os
contatos de uma categoria, ordenados por nome.
'''

def lifp04():
    agenda = {
        'família': [
            ('Ana Silva', '1234-5678', 'família'),
            ('Bruno Costa', '2345-6789', 'família')
        ],
        'trabalho': [
            ('Carlos Souza', '3456-7890', 'trabalho'),
            ('Diego Lima', '4567-8901', 'trabalho')
        ],
        'amigos': [
            ('Fernanda Melo', '5678-9012', 'amigos'),
            ('Gabriel Alves', '6789-0123', 'amigos')
        ]
    }

    categoria_buscada = input("Digite a categoria (família, trabalho, amigos): ").lower()

    if categoria_buscada in agenda:
        contatos = agenda[categoria_buscada]
    else:
        print("Categoria não encontrada.")
        return []

    contatos_ordenados = sorted(contatos)
    
    print(f"\n--- Contatos da categoria '{categoria_buscada}' ordenados por nome ---")

    if not contatos_ordenados:
        print("Nenhum contato encontrado para esta categoria.")
    else:
        for contato in contatos_ordenados:
            nome, telefone, categoria = contato
            print(f"👤 Nome: {nome} | 📞 Telefone: {telefone}")

'''
Exercício 5 — Classe Usuario com validação encapsulada
Crie uma classe Usuario com atributos nome, email e senha (privado). Use @property e
@senha.setter para validar que a senha tenha pelo menos 8 caracteres antes de ser
aceita. Implemente um método verificar_senha(tentativa) que retorna True ou False
sem nunca expor a senha real.
'''

def lifp05():
    class Usuario:
        def __init__(self, nome, email, senha):
            self.nome = nome
            self.email = email
            self.senha = senha

        @property
        def senha(self):
            return "******** (Acesso privado)"

        @senha.setter
        def senha(self, nova_senha):
            if len(nova_senha) < 8:
                raise ValueError("A senha deve ter pelo menos 8 caracteres.")
            self.__senha = nova_senha

        def verificar_senha(self, tentativa):
            return self.__senha == tentativa

    print("--- Criando um usuário válido ---")
    # Criando usuário com senha de 8 caracteres (funcionará normalmente)
    user = Usuario("Carlos Silva", "carlos@email.com", "senha123")
    print(f"Usuário criado: {user.nome}")
    print(f"E-mail: {user.email}")
    print(f"Tentativa de ler a senha diretamente: {user.senha}")

    print("\n--- Testando a verificação de senha ---")
    print(f"Testando '123456': {user.verificar_senha('123456')}")  # Retorna False
    print(f"Testando 'senha123': {user.verificar_senha('senha123')}")  # Retorna True

    print("\n--- Testando a validação (senha curta) ---")
    try:
        # Tentando alterar a senha para uma menor do que 8 caracteres
        user.senha = "12345"
    except ValueError as erro:
        print(f"❌ Erro capturado com sucesso: {erro}")

'''
Exercício 6 — Menu interativo de tarefas
Crie um menu com um laço while que ofereça as opções:
1) Adicionar tarefa,
2) Listar tarefas,
3) Remover tarefa,
4) Sair.
Cada tarefa deve ser representada por um objeto de uma classe Tarefa com os
seguintes atributos: descricao (texto da tarefa), concluida (booleano, inicia como False)
e data_criacao (uma tupla representando uma data). A classe Tarefa deve ter pelo
menos um método, como marcar_concluida(), que altera o atributo concluida para True,
e um método __str__ (ou um método descricao_completa()) que retorna uma
representação textual da tarefa incluindo seu status (pendente/concluída).
As tarefas devem ser armazenadas em uma lista de objetos Tarefa, que persiste
enquanto o menu roda. A opção 'Listar tarefas' deve percorrer essa lista e imprimir a
descrição completa de cada uma.
'''

def lifp06():
    class Tarefa:
        def __init__(self, descricao:str="", concluida:bool=False):
            self.descricao = descricao
            self.concluida = concluida
            hoje = datetime.date.today()
            self.data_criacao = (hoje.day, hoje.month, hoje.year)

        def __str__(self):
            status = "Concluída" if self.concluida else "Pendente"
            dia, mes, ano = self.data_criacao
            data_formatada = f"{dia:02d}/{mes:02d}/{ano}"
            
            return f"[{status}] {self.descricao} (Criada em: {data_formatada})"

        def marcar_concluida(self):
            self.concluida = True

    lista_tarefas = []

    while True:
        print("\n--- Menu de Tarefas ---")
        print("1) Adicionar tarefa")
        print("2) Listar tarefas")
        print("3) Remover tarefa")
        print("4) Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição da tarefa: ")
            tarefa = Tarefa(descricao)
            lista_tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")

        elif opcao == '2':
            if not lista_tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                print("\n--- Lista de Tarefas ---")
                for idx, tarefa in enumerate(lista_tarefas):
                    print(f"{idx + 1}. {tarefa}")

        elif opcao == '3':
            if not lista_tarefas:
                print("Nenhuma tarefa para remover.")
            else:
                for idx, tarefa in enumerate(lista_tarefas):
                    print(f"{idx + 1}. {tarefa}")
                try:
                    indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
                    if 0 <= indice < len(lista_tarefas):
                        lista_tarefas.pop(indice)
                        print("Tarefa removida com sucesso!")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")

        elif opcao == '4':
            print("Saindo do menu de tarefas... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

lifp06()