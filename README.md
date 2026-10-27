# 📚 Sistema de Gerenciamento de Biblioteca

## 📝 Sobre o projeto

Este projeto consiste em um sistema de gerenciamento de biblioteca desenvolvido em Python, com o objetivo de facilitar o controle de livros, usuários, empréstimos, devoluções e multas por atraso.

O sistema funciona por meio de um menu interativo no terminal, permitindo que o usuário escolha as operações desejadas de forma simples e organizada.

## 🚀 Funcionalidades

* Cadastro de usuários: permite cadastrar usuários com nome e e-mail, evitando e-mails duplicados.
* Adição de livros: permite adicionar novos livros ao acervo, evitando títulos duplicados.
* Pesquisa de livros: possibilita pesquisar livros pelo título ou nome do autor.
* Listagem de livros: exibe todos os livros cadastrados e informa se estão disponíveis ou emprestados.
* Empréstimo de livros: registra o empréstimo de um livro para um usuário cadastrado.
* Devolução de livros: registra a devolução e verifica se houve atraso.
* Listagem de empréstimos: apresenta os empréstimos registrados, suas datas e seus status.
* Cálculo de multas: calcula as multas por atraso, considerando os empréstimos devolvidos e os que continuam em aberto.

## 🛠️ Tecnologias utilizadas

* Python 3
* Módulo datetime
* Estruturas de dados: listas e dicionários
* Funções e estruturas de repetição e decisão

## ⚙️ Regras do sistema

* O prazo de empréstimo é de 21 dias.
* A multa por atraso é de R$ 2,00 por dia.
* Somente usuários cadastrados podem realizar empréstimos.
* Um livro não pode ser emprestado novamente enquanto houver um empréstimo ativo.
* A devolução registra a data real e calcula a multa, quando aplicável.
* O cálculo de multas considera os dias de atraso até a data atual para empréstimos ainda em aberto.

## 📖 Livros iniciais

O sistema começa com 12 livros cadastrados, incluindo:

* Dom Casmurro — Machado de Assis
* O Pequeno Príncipe — Antoine de Saint-Exupéry
* 1984 — George Orwell
* Dom Quixote — Miguel de Cervantes
* A Divina Comédia — Dante Alighieri
* Guerra e Paz — Liev Tolstói
* Cem Anos de Solidão — Gabriel García Márquez
* Crime e Castigo — Fiódor Dostoiévski
* Orgulho e Preconceito — Jane Austen
* Memórias Póstumas de Brás Cubas — Machado de Assis
* Vidas Secas — Graciliano Ramos
* Capitães da Areia — Jorge Amado

## 💻 Como executar o projeto

Pré-requisitos

Ter o Python 3 instalado no computador.

Passo a passo

1. Clone o repositório:

git clone URL_DO_SEU_REPOSITORIO

2. Entre na pasta do projeto:

cd NOME_DA_PASTA

3. Execute o arquivo Python:

python main.py

    Caso necessário, utilize:

python3 main.py

    Observação: substitua main.py pelo nome real do arquivo que contém o código.

## 📋 Menu do sistema

Ao executar o programa, será exibido o seguinte menu:

=== BIBLIOTECA ===
1 - Cadastrar usuário
2 - Adicionar livro
3 - Pesquisar livros
4 - Listar livros
5 - Emprestar livro
6 - Devolver livro
7 - Listar empréstimos
8 - Calcular multas
0 - Sair

Basta digitar o número correspondente à operação desejada.

## 📂 Estrutura do projeto

biblioteca/
├── main.py
└── README.md

A estrutura acima é uma sugestão para organizar os arquivos do projeto.

## ⚠️ Limitações atuais

* Os dados são armazenados em memória e são perdidos quando o programa é encerrado.
* O sistema funciona apenas pelo terminal.
* A identificação de usuários e livros é realizada por nome e título, respectivamente.
* O sistema não possui banco de dados nem interface gráfica.

## 🔮 Melhorias futuras

* Integrar um banco de dados, como SQLite ou MySQL.
* Criar uma interface gráfica ou aplicação web.
* Implementar login e autenticação de usuários.
* Gerar relatórios de empréstimos e multas.
* Permitir a consulta do histórico de cada usuário.
* Adicionar testes automatizados.

## 🎯 Objetivo acadêmico

O projeto tem como finalidade aplicar conceitos fundamentais de programação em Python, como funções, listas, dicionários, condicionais, laços de repetição, manipulação de datas e organização da lógica de um sistema.

## 👩‍💻 Autoria

Alunos
* Marcela Geovana
* João Pedro Santos
* Ana Jamilly
* Taislayne
* Emily Lima

⸻

Desenvolvido com Python 🐍
