
from datetime import date, timedelta

# Configurações da biblioteca
PRAZO_EMPRESTIMO = 21
MULTA_POR_DIA = 2.00

# Lista de livros iniciais
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


def cadastrar_usuario():
    print("\n--- CADASTRO DE USUÁRIO ---")
    nome = input("Digite o nome do usuário: ").strip()
    email = input("Digite o e-mail: ").strip()

    if not nome or not email:
        print("Nome e e-mail são obrigatórios.")
        return

    for usuario in usuarios:
        if usuario["email"].lower() == email.lower():
            print("Este e-mail já está cadastrado.")
            return

    usuarios.append({"nome": nome, "email": email})
    print("\nUsuário cadastrado com sucesso!")


def pesquisar_livros():
    print("\n--- PESQUISAR LIVROS ---")
    pesquisa = input("Digite o título ou autor: ").strip().lower()

    if not pesquisa:
        print("Digite algo para pesquisar.")
        return

    encontrado = False
    for livro in livros:
        if pesquisa in livro["titulo"].lower() or pesquisa in livro["autor"].lower():
            print("\nTítulo:", livro["titulo"])
            print("Autor:", livro["autor"])
            encontrado = True

    if not encontrado:
        print("\nNenhum livro encontrado.")


def adicionar_livro():
    print("\n--- ADICIONAR LIVRO ---")
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o nome do autor: ").strip()

    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return

    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            print("Este livro já está cadastrado.")
            return

    livros.append({"titulo": titulo, "autor": autor})
    print("\nLivro adicionado com sucesso!")


def buscar_usuario(nome):
    for usuario in usuarios:
        if usuario["nome"].lower() == nome.lower():
            return usuario
    return None


def buscar_livro(titulo):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            return livro
    return None


def emprestar_livro():
    print("\n--- EMPRÉSTIMO DE LIVRO ---")
    nome_usuario = input("Digite o nome do usuário: ").strip()
    titulo_livro = input("Digite o título do livro: ").strip()

    usuario = buscar_usuario(nome_usuario)
    if usuario is None:
        print("\nUsuário não encontrado.")
        return

    livro = buscar_livro(titulo_livro)
    if livro is None:
        print("\nLivro não encontrado.")
        return

    for emprestimo in emprestimos:
        if emprestimo["titulo"].lower() == titulo_livro.lower() and not emprestimo["devolvido"]:
            print("\nEste livro já está emprestado.")
            return

    data_emprestimo = date.today()
    data_devolucao = data_emprestimo + timedelta(days=PRAZO_EMPRESTIMO)

    emprestimos.append({
        "usuario": usuario["nome"],
        "email": usuario["email"],
        "titulo": livro["titulo"],
        "autor": livro["autor"],
        "data_emprestimo": data_emprestimo.isoformat(),
        "data_devolucao_prevista": data_devolucao.isoformat(),
        "devolvido": False
    })

    print(f"\nEmpréstimo registrado com sucesso para {usuario['nome']}.")


def devolver_livro():
    print("\n--- DEVOLUÇÃO DE LIVRO ---")
    titulo_livro = input("Digite o título do livro para devolver: ").strip()

    for emprestimo in emprestimos:
        if emprestimo["titulo"].lower() == titulo_livro.lower() and not emprestimo["devolvido"]:
            data_devolucao = date.today()
            data_prevista = date.fromisoformat(emprestimo["data_devolucao_prevista"])
            emprestimo["devolvido"] = True
            emprestimo["data_devolucao_real"] = data_devolucao.isoformat()

            if data_devolucao > data_prevista:
                dias_atraso = (data_devolucao - data_prevista).days
                multa = dias_atraso * MULTA_POR_DIA
                print(f"\nLivro devolvido com atraso. Multa: R$ {multa:.2f}.")
            else:
                print("\nLivro devolvido dentro do prazo.")
            return

    print("\nNenhum empréstimo ativo encontrado para este livro.")


def listar_livros():
    print("\n--- LISTA DE LIVROS ---")
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        titulo = livro["titulo"]
        autor = livro["autor"]

        emprestado = False
        for emprestimo in emprestimos:
            if emprestimo["titulo"].lower() == titulo.lower() and not emprestimo["devolvido"]:
                emprestado = True
                break

        status = "Emprestado 🔴" if emprestado else "Disponível 🟢"
        print(f"• Título: {titulo} | Autor: {autor} | Status: {status}")


def listar_emprestimos():
    print("\n--- EMPRÉSTIMOS ---")
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
        return

    for emprestimo in emprestimos:
        status = "Devolvido" if emprestimo["devolvido"] else "Em aberto"
        print(
            f"• Usuário: {emprestimo['usuario']} | "
            f"Livro: {emprestimo['titulo']} | "
            f"Data do empréstimo: {emprestimo['data_emprestimo']} | "
            f"Prazo: {emprestimo['data_devolucao_prevista']} | "
            f"Status: {status}"
        )


# NOVA FUNÇÃO: CALCULAR MULTAS
def calcular_multas():
    print("\n--- CÁLCULO DE MULTAS ---")

    if not emprestimos:
        print("Nenhum empréstimo registrado.")
        return

    total_multas = 0.0

    for emprestimo in emprestimos:
        data_prevista = date.fromisoformat(
            emprestimo["data_devolucao_prevista"]
        )

        # Se devolvido, utiliza a data real.
        # Se ainda estiver emprestado, utiliza a data atual.
        if emprestimo["devolvido"]:
            data_final = date.fromisoformat(
                emprestimo["data_devolucao_real"]
            )
        else:
            data_final = date.today()

        dias_atraso = max(
            0, (data_final - data_prevista).days
        )

        multa = dias_atraso * MULTA_POR_DIA
        total_multas += multa

        status = (
            "Devolvido"
            if emprestimo["devolvido"]
            else "Em aberto"
        )

        print(f"\nLivro: {emprestimo['titulo']}")
        print(f"Usuário: {emprestimo['usuario']}")
        print(f"Status: {status}")
        print(f"Prazo de devolução: {data_prevista.strftime('%d/%m/%Y')}")
        print(f"Dias de atraso: {dias_atraso}")
        print(f"Multa calculada: R$ {multa:.2f}")

    print("\n------------------------------")
    print(f"TOTAL DE MULTAS: R$ {total_multas:.2f}")


def menu():
    while True:
        print("\n=== BIBLIOTECA ===")
        print("1 - Cadastrar usuário")
        print("2 - Adicionar livro")
        print("3 - Pesquisar livros")
        print("4 - Listar livros")
        print("5 - Emprestar livro")
        print("6 - Devolver livro")
        print("7 - Listar empréstimos")
        print("8 - Calcular multas")  # NOVA OPÇÃO
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            adicionar_livro()
        elif opcao == "3":
            pesquisar_livros()
        elif opcao == "4":
            listar_livros()
        elif opcao == "5":
            emprestar_livro()
        elif opcao == "6":
            devolver_livro()
        elif opcao == "7":
            listar_emprestimos()
        elif opcao == "8":
            calcular_multas()  # CHAMA A NOVA FUNÇÃO
        elif opcao == "0":
            print("\nSistema encerrado.")
            break
        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    menu()
