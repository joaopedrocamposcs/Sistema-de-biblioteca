from datetime import date, timedelta

#Configurações da biblioteca
PRAZO_EMPRESTIMO = 21
MULTA_POR_DIA = 2.00

#ista de sistemas
livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"},
    {"titulo": "1984", "autor": "George Orwell"},
    {"titulo": "Dom Quixote", "autor": "Miguel de Cervantes"},
    {"titulo": "A Divina Comédia", "autor": "Dante Alighieri"},
    {"titulo": "Guerra e Paz", "autor": "Liev Tolstói"},
    {"titulo": "Cem Anos de Solidão", "autor": "Gabriel García Márquez"},
    {"titulo": "Crime e Castigo", "autor": "Fiódor Dostoiévski"},
    {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen"},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis"},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos"},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado"}
]

usuarios = []
emprestimos = []

#cadastrar usuarios
def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    usuario = {
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)

    print("\nUsuário cadastrado com sucesso!")

#pesquisar livros
def pesquisar_livros():
    print("\n--- PESQUISAR LIVROS ---")
    pesquisa = input("Digite  título ou autor:").lower()
    encontrado = False

    for livro in livros:
        if (pesquisa in livro["titulo"].lower()
            or pesquisa in livro["autor"].lower()):
            print("\nTítulo:", livro["titulo"])
            print("Autor:", livro["autor"])
            encontrado = True

    if not encontrado:
        print("\nNenhum livro encontrado.")

#adicionar livro
def adicionar_livro():
    print("\n--- ADIOCIONAR LIVRO ---")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")

    livro = {
        "titulo": titulo,
        "autor": autor
    }

    livros.append(livro)
    print("\nLivro adicionado com sucesso!")

#realizar empréstimo
def emprestar_livro():
    print("\n--- EMPRÉTIMO DE LIVRO ---")
    nome_usuario = input("Digite o nome do usuário: ")
    titulo_livro = input("Digite o título do livro: ")

    livro_encontrado = None

    for livro in livros:
        if livro["titulo"].lower() == titulo_livro.lower():
            livro_encontrado = livro
            break
    if livro_encontrado is None:
        print("\nLivro não encontrado.")
        return
    #verificar se o livro já foi emprestado
    for emprestimo in emprestimos:
        if (emprestimo["título"].lower() == titulo_livro.lower()
            and emprestimo["devolvido"] == False):
            print("\nEste livro já está alugado.")
            return
    #registrar datas
