# IMPORTAÇÃO DAS BIBLIOTECAS

import os
from colorama import Fore, Back, Style, init

# Inicializa o Colorama
init(autoreset=True)

# CLASSE CLIENTE

class Cliente:

    def __init__(self, nome, email, telefone):

        self.nome = nome
        self.email = email
        self.telefone = telefone

# CLASSE DO SISTEMA

class SistemaCadastro:

    def __init__(self):

        self.clientes = []

        self.carregar_clientes()

    # Carrega clientes do arquivo
    def carregar_clientes(self):

        if not os.path.exists("cliente.txt"):

            return

        with open(

            "cliente.txt",

            "r",

            encoding="utf-8"

        ) as arquivo:

            linhas = arquivo.readlines()

            for linha in linhas:

                dados = linha.strip().split(";")

                if len(dados) == 3:

                    nome = dados[0].replace(
                        "Nome: ",
                        ""
                    ).strip()

                    email = dados[1].replace(

                        "E-mail: ",
                        ""

                    ).strip()

                    telefone = dados[2].replace(

                        "Telefone: ",
                        ""

                    ).strip()

                    cliente = Cliente(

                        nome,

                        email,

                        telefone

                    )

                    self.clientes.append(

                        cliente

                    )

    # Salvar cliente
    def salvar_arquivo(self, cliente):

        with open(

            "cliente.txt",

            "a",

            encoding="utf-8"

        ) as arquivo:

            arquivo.write(

                f"Nome: {cliente.nome}; "

                f"E-mail: {cliente.email}; "

                f"Telefone: {cliente.telefone}\n"

            )

    # Atualizar arquivo
    def atualizar_arquivo(self):

        with open(

            "cliente.txt",

            "w",

            encoding="utf-8"

        ) as arquivo:

            for cliente in self.clientes:

                arquivo.write(

                    f"Nome: {cliente.nome}; "

                    f"E-mail: {cliente.email}; "

                    f"Telefone: {cliente.telefone}\n"

                )

    # Cadastro
    def cadastrar_cliente(self):

        print(

            Fore.CYAN +

            "\n===== CADASTRO DE CLIENTE ====="

        )

        while True:

            nome = input(

                "Nome: "

            ).strip()

            if nome == "":

                print(

                    Fore.RED +

                    "Nome obrigatório."

                )

            else:

                break

        while True:

            email = input(

                "E-mail: "

            ).strip()

            if (

                email.count("@") != 1

                or "." not in email.split("@")[1]

            ):

                print(

                    Fore.RED +

                    "E-mail inválido."

                )

            else:

                break

        while True:

            telefone = input(

                "Telefone: "

            ).strip()

            if not telefone.isdigit():

                print(

                    Fore.RED +

                    "Digite apenas números."

                )

            elif len(telefone) < 9 or len(telefone) >= 12:

                print(

                    Fore.RED +

                    "O telefone deve ter entre 9 e 11 dígitos."

                )

            else:

                break

        cliente = Cliente(

            nome,

            email,

            telefone

        )

        self.clientes.append(

            cliente

        )

        self.salvar_arquivo(

            cliente

        )

        print(

            Fore.GREEN +

            "\nCliente cadastrado com sucesso!"

        )

    # Listagem
    def listar_clientes(self):

        print(

            Fore.CYAN +

            "\n===== CLIENTES ====="

        )

        if len(self.clientes) == 0:

            print(

                Fore.YELLOW +

                "Nenhum cliente cadastrado."

            )

            return

        for i, cliente in enumerate(

            self.clientes,

            start=1

        ):

            print(

                Fore.BLUE +

                "\n════════════════════"

            )

            print(

                Fore.YELLOW +

                f"Cliente {i}"

            )

            print(

                Fore.BLUE +

                "════════════════════"

            )

            print(

                Fore.GREEN +

                f"Nome: {cliente.nome}"
            )


            print(

                Fore.MAGENTA +

                f"E-mail: {cliente.email}"

            )

            print(

                Fore.YELLOW +

                f"Telefone: {cliente.telefone}"

            )

    # Editar cliente
    def editar_cliente(self):

        self.listar_clientes()

        if len(self.clientes) == 0:

            return

        try:

            indice = int(

                input(

                    "\nCliente: "

                )

            ) - 1

            if indice < 0 or indice >= len(self.clientes):

                print(

                    Fore.RED +

                    "Cliente inválido."

                )

                return

            cliente = self.clientes[indice]

            nome = input(

                f"Nome ({cliente.nome}): "

            ).strip()

            if nome != "":

                cliente.nome = nome

            email = input(

                f"E-mail ({cliente.email}): "

            ).strip()

            if email != "":

                cliente.email = email

            telefone = input(

                f"Telefone ({cliente.telefone}): "

            ).strip()

            if telefone != "":

                cliente.telefone = telefone

            self.atualizar_arquivo()

            print(

                Fore.GREEN +

                "Cliente atualizado!"

            )

        except ValueError:

            print(

                Fore.RED +

                "Valor inválido."

            )

    # Excluir cliente
    def excluir_cliente(self):

        self.listar_clientes()

        if len(self.clientes) == 0:

            return

        try:

            indice = int(

                input(

                    "\nCliente: "

                )

            ) - 1

            if indice < 0 or indice >= len(self.clientes):

                print(

                    Fore.RED +

                    "Cliente inválido."

                )

                return

            confirmar = input(

                "Deseja excluir? (s/n): "

            ).lower()

            if confirmar != "s":

                print(

                    Fore.YELLOW +

                    "Operação cancelada."

                )

                return

            removido = self.clientes.pop(

                indice

            )

            self.atualizar_arquivo()

            print(

                Fore.GREEN +

                f"{removido.nome} removido!"

            )

        except ValueError:

            print(

                Fore.RED +

                "Digite apenas números."

            )

    # Menu
    def executar(self):

        while True:

            print(

                Fore.CYAN +

                "\n═══════════════════════"

            )

            print(

                Fore.WHITE +

                " SISTEMA DE CLIENTES "

            )

            print(

                Fore.WHITE +

                "═══════════════════════"
            )

            print(

                Fore.GREEN +

                "1 - Cadastrar Cliente"
            )
            print(
                Fore.BLUE +
                "2 - Listar Clientes"
            )
            print(
                Fore.MAGENTA +
                "3 - Editar Cliente"
            )
            print(
                Fore.RED +
                "4 - Excluir Cliente"
            )
            print(
                 Fore.YELLOW +

                "0 - Sair"
            )
            try:
                opcao = int(

                    input(

                        "\nEscolha: "

                    )

                )

                if opcao == 1:
                    self.cadastrar_cliente()

                elif opcao == 2:
                    self.listar_clientes()

                elif opcao == 3:
                    self.editar_cliente()

                elif opcao == 4:
                    self.excluir_cliente()

                elif opcao == 0:

                    print(
                        Fore.GREEN +
                        "\nSistema encerrado."

                    )

                    break

                else:

                    print(
                        Fore.RED +
                        "Opção inválida."

                    )

            except ValueError:

                print(
                    Fore.RED +
                    "Digite apenas números."

                )

# PROGRAMA PRINCIPAL

sistema = SistemaCadastro()

sistema.executar()

print(Style.RESET_ALL)