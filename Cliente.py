import os
from colorama import Fore, init

init(autoreset=True)

class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class SistemaCadastro:
    def __init__(self):
        self.clientes = []
        self.arquivo = "clientes.txt"

        print("O arquivo será salvo em:")
        print(os.path.abspath(self.arquivo))

        self.carregar()

    def carregar(self):
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(";")
                    if len(dados) == 3:
                        self.clientes.append(Cliente(*dados))
        except FileNotFoundError:
            pass

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            for cliente in self.clientes:
                arquivo.write(
                    f"{cliente.nome};{cliente.email};{cliente.telefone}\n"
                )

    def cadastrar(self):
        print()
        print(Fore.YELLOW + "CADASTRO DE CLIENTE")
        print()

        while True:
            nome = input("Nome: ").strip()
            if nome and all(c.isalpha() or c.isspace() for c in nome):
                break
            print(Fore.RED + "Digite um nome válido.")

        while True:
            email = input("E-mail: ").strip()
            if "@" in email and "." in email.split("@")[-1]:
                break
            print(Fore.RED + "Digite um e-mail válido.")

        while True:
            telefone = input("Telefone: ").strip()
            if telefone.isdigit() and 9 <= len(telefone) <= 11:
                break
            print(Fore.RED + "Digite um telefone válido.")

        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        self.salvar()

        print(Fore.GREEN + "Cliente cadastrado com sucesso!")

    def listar(self):
        print()
        print(Fore.YELLOW + "LISTA DE CLIENTES")
        print()

        if not self.clientes:
            print("Não tem nenhum cliente cadastrado.")
            return

        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i} - {cliente.nome}")
            print(f"    E-mail: {cliente.email}")
            print(f"    Telefone: {cliente.telefone}")

    def editar(self):
        if not self.clientes:
            print("Não tem nenhum cliente cadastrado.")
            return

        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i} - {cliente.nome}")

        try:
            cliente = self.clientes[int(input("Escolha o cliente: ")) - 1]
        except (ValueError, IndexError):
            print(Fore.RED + "Cliente inválido.")
            return

        nome = input(f"Novo nome ({cliente.nome}): ").strip()
        email = input(f"Novo e-mail ({cliente.email}): ").strip()
        telefone = input(f"Novo telefone ({cliente.telefone}): ").strip()

        if nome:
            cliente.nome = nome
        if email:
            cliente.email = email
        if telefone:
            cliente.telefone = telefone

        self.salvar()
        print(Fore.GREEN + "Cliente alterado com sucesso!")

    def excluir(self):
        if not self.clientes:
            print("Não tem nenhum cliente cadastrado.")
            return

        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i} - {cliente.nome}")

        try:
            numero = int(input("Escolha o cliente: ")) - 1
            cliente = self.clientes[numero]
        except (ValueError, IndexError):
            print(Fore.RED + "Cliente inválido.")
            return

        if input("Tem certeza? (s/n): ").lower() == "s":
            self.clientes.pop(numero)
            self.salvar()
            print(Fore.GREEN + f"{cliente.nome} foi excluído.")

    def executar(self):
        while True:
            print()
            print(Fore.YELLOW + "SISTEMA DE CADASTRO")
            print()
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Editar cliente")
            print("4 - Excluir cliente")
            print("0 - Sair")
            print()

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.editar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "0":
                print(Fore.GREEN + "Programa encerrado.")
                break
            else:
                print(Fore.RED + "Opção inválida.")

sistema = SistemaCadastro()
sistema.executar()
