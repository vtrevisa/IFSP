'''
Exercício 1 — Itens do acervo
Modele um pequeno sistema de biblioteca aplicando os 4 pilares:
Abstração: crie uma classe ItemAcervo com uma interface simples (emprestar(),
devolver(), esta_disponivel()), escondendo os detalhes de controle de disponibilidade.
Encapsulamento: o status de disponibilidade deve ser um atributo privado, alterado
apenas pelos métodos da classe.
Herança: crie subclasses Livro e Revista a partir de ItemAcervo, cada uma com atributos
próprios (por exemplo, autor para Livro e edicao para Revista).
Polimorfismo: sobrescreva um método descricao() em cada subclasse e escreva uma
função que imprime a descrição de uma lista de itens de tipos diferentes, sem verificar o
tipo de cada objeto.
'''
def lo4pi01():
    class ItemAcervo:
        def __init__(self, name, disponivel = False):
            self.nome = name
            self.__disponivel = disponivel
        
        def emprestar(self):
            if self.__disponivel == False:
                return "Já emprestamos todos os exemplares!"
            self.__disponivel = False

        def devolver(self):
            if self.__disponivel == True:
                return "Livro já devolvido!"
            self.__disponivel = True

        def esta_disponivel(self):
            if self.__disponivel == True:
                return "Disponível"
            else:
                return "Indisponível"

        def descricao(self):
            print("Sou apenas um item indefinido.")

    class Livro(ItemAcervo):
        def __init__(self, autor, name, disponivel:bool):
            super().__init__(name, disponivel)
            self.autor = autor

        def descricao(self):
            disp = self.esta_disponivel()
            return f"Livro {self.nome} do autor: {self.autor} está {disp}"
        
    class Revista(ItemAcervo):
        def __init__(self, edicao, name, disponivel:bool):
            super().__init__(name, disponivel)
            self.edicao = edicao

        def descricao(self):
            disp = self.esta_disponivel()
            return f"Revista {self.nome} de edição: {self.edicao} está {disp}"

    lista = [
         Livro( "Autor 1", "nome 1", True),
         Revista("09", "Revista 1", True),
         Livro("Autor 2", "nome 2", False),
         Revista("10", "Revista 2", False),
    ]

    for l in lista:
         print(l.descricao())

'''
Exercício 2 — Extensão do projeto — Classe Biblioteca
Crie uma classe Biblioteca responsável por gerenciar uma lista de itens do acervo,
utilizando os itens criados no Exercício 1. A classe deve armazenar internamente os
objetos do acervo e implementar métodos para adicionar novos itens, remover itens,
listar todos os itens cadastrados, buscar itens por título e controlar operações de
empréstimo e devolução chamando os métodos emprestar() e devolver() dos próprios
itens. Garanta que as regras de disponibilidade continuem encapsuladas na classe
ItemAcervo, de modo que a Biblioteca apenas coordene o gerenciamento da coleção.
'''
def lo4pi02():
    class ItemAcervo:
        def __init__(self, name, disponivel = False):
            self.nome = name
            self.__disponivel = disponivel
        
        def emprestar(self):
            if self.__disponivel == False:
                return "Já emprestamos todos os exemplares!"
            self.__disponivel = False
            return "Item emprestado com sucesso!"

        def devolver(self):
            if self.__disponivel == True:
                return "Item já devolvido!"
            self.__disponivel = True
            return "Item devolvido com sucesso!"

        def esta_disponivel(self):
            if self.__disponivel == True:
                return "Disponível"
            else:
                return "Indisponível"

        def descricao(self):
            print("Sou apenas um item indefinido.")

    class Livro(ItemAcervo):
        def __init__(self, autor, name, disponivel:bool):
            super().__init__(name, disponivel)
            self.autor = autor

        def descricao(self):
            disp = self.esta_disponivel()
            return f"Livro {self.nome} do autor: {self.autor} está {disp}"
        
    class Revista(ItemAcervo):
        def __init__(self, edicao, name, disponivel:bool):
            super().__init__(name, disponivel)
            self.edicao = edicao

        def descricao(self):
            disp = self.esta_disponivel()
            return f"Revista {self.nome} de edição: {self.edicao} está {disp}"

    class Biblioteca:
        def __init__(self, items:list):
            self.items = items

        def adicionar_item(self, item:object):
            self.items.append(item)

        def remover_item(self, item):
            for i in self.items:
                if i == item:
                    self.items.remove(item)

        def listar_items(self):
            for i in self.items:
                print(i.descricao())

        def buscar_item(self, nome):
            for i in self.items:
                if i.nome == nome:
                    print(f"Volume '{i.nome}' encontrado!")
                    print(i.descricao())

        def emprestar(self, item):
            for i in self.items:
                if i == item:
                    print(i.emprestar())


        def devolver(self, item):
            for i in self.items:
                if i == item:
                    print(i.devolver())

    print("\n" + "="*40)
    print("      INICIANDO TESTES DA BIBLIOTECA    ")
    print("="*40)

    # 1. Criando itens de teste
    livro1 = Livro("George Orwell", "1984", True)
    livro2 = Livro("J.R.R. Tolkien", "O Hobbit", False)
    revista1 = Revista("Ed. 150", "Superinteressante", True)

    # 2. Inicializando a biblioteca com uma lista contendo livro1 e livro2
    print("\n--- Teste 1: Inicializando Biblioteca ---")
    minha_biblioteca = Biblioteca([livro1, livro2])
    minha_biblioteca.listar_items()

    # 3. Testando o método adicionar_item
    print("\n--- Teste 2: Adicionando Nova Revista ---")
    minha_biblioteca.adicionar_item(revista1)
    minha_biblioteca.listar_items()

    # 4. Testando o método buscar_item
    print("\n--- Teste 3: Buscando Item por Nome ---")
    minha_biblioteca.buscar_item("O Hobbit")

    # 5. Testando operações de Empréstimo
    print("\n--- Teste 4: Controlando Empréstimos ---")
    print("Tentando emprestar livro disponível (1984):")
    minha_biblioteca.emprestar(livro1) # Deve dar sucesso
    
    print("\nTendando emprestar livro indisponível (1984):")
    minha_biblioteca.emprestar(livro1) # Deve dar erro de indisponível

    # 6. Testando operações de Devolução
    print("\n--- Teste 5: Controlando Devoluções ---")
    print("Tentando devolver livro que foi emprestado (1984):")
    minha_biblioteca.devolver(livro1) # Deve dar sucesso
    
    print("\nTentando devolver livro que já estava disponível (Superinteressante):")
    minha_biblioteca.devolver(revista1) # Deve dizer que já foi devolvido

    # 7. Testando o método remover_item
    print("\n--- Teste 6: Removendo um Item ---")
    print("Removendo 'O Hobbit' do acervo...")
    minha_biblioteca.remover_item(livro2)
    
    print("\nEstado final do acervo:")
    minha_biblioteca.listar_items()
    print("="*40)

lo4pi02()