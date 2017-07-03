#-------Trabalho Final - PRA em Python v2.x----
#Eduardo Hofelmann
#Jonathan de Oliveira Cardoso
#Marcos Valdecir Cavalheiro Jr
#Mateus Leite Bittencourt
#----------------------------------------------

from IncluiCommand import IncluiCommand
from EditaCommand import EditaCommand
from RemoverCommand import RemoverCommand
from MostrarCommand import MostrarCommand
from Autor import Autor
from Leitor import Leitor
from Livro import Livro
from AutoresLivros import AutoresLivros


if __name__ == '__main__':
    print ("*** SISTEMA BIBLIOTECARIO ***\n")

    while(1):
        print("1- INSERIR")
        print("2- EDITAR")
        print("3- REMOVER")
        print("4- Mostrar Elementos")
        print("0- Sair\n")

        opc = input("Qual operacao deseja realizar: ")

        if opc == 0:
            print ("Obrigado, volte sempre!")
            break

        if opc == 1:
            print("1- Autor")
            print("2- Leitor")
            print("3- Livro")
            print("4- Autor do Livro\n")

            sub_op = input("Qual Entidade deseja incluir: ")

            if sub_op == 1:
                nome = raw_input("Digite o nome do autor: ")
                cod = raw_input("De um codigo para ele: ")

                autor = Autor(cod, nome)

                novo_autor = IncluiCommand(sub_op, autor)
                novo_autor.execute(sub_op)

            if sub_op == 2:
                nome = raw_input("Digite o nome do leitor: ")
                cod = raw_input("De um codigo para ele: ")

                leitor = Leitor(cod, nome)

                novo_leitor = IncluiCommand(sub_op, leitor)
                novo_leitor.execute(sub_op)

            if sub_op == 3:
                titulo = raw_input("Digite o titulo do livro: ")
                cod = raw_input("De um codigo do livro: ")

                livro = Livro(cod, titulo)

                novo_livro = IncluiCommand(sub_op, livro)
                novo_livro.execute(sub_op)

            if sub_op == 4:
                codL = raw_input("Digite o codigo do livro: ")
                codA = raw_input("Agora digite o codigo do autor: ")

                autor_livro = AutoresLivros(codL, codA)

                novo_autor_livro = IncluiCommand(sub_op, autor_livro)
                novo_autor_livro.execute(sub_op)

        if opc == 2:
            print("1- Autor")
            print("2- Leitor")
            print("3- Livro")
            print("4- Autor do Livro\n")

            sub_op = input("Qual Entidade deseja editar: ")

            if sub_op == 1:
                cod = raw_input("De o codigo do autor que deseja editar: ")
                nome = raw_input("Edite o nome do autor: ")


                autor = Autor(cod, nome)

                edita_autor = EditaCommand(sub_op, autor)
                edita_autor.execute(sub_op)

            if sub_op == 2:
                cod = raw_input("De o codigo do leitor que deseja editar: ")
                nome = raw_input("Edite o nome do leitor: ")

                leitor = Leitor(cod, nome)

                edita_leitor = EditaCommand(sub_op, leitor)
                edita_leitor.execute(sub_op)

            if sub_op == 3:
                titulo = raw_input("Digite o titulo do livro: ")
                cod = raw_input("De um codigo do livro: ")

                livro = Livro(cod, titulo)

                novo_livro = IncluiCommand(sub_op, livro)
                novo_livro.execute(sub_op)

            if sub_op == 4:
                codL = raw_input("Digite o codigo do livro: ")
                codA = raw_input("Atualize o autor inserindo o codigo do mesmo: ")

                autor_livro = AutoresLivros(codL, codA)

                novo_autor_livro = IncluiCommand(sub_op, autor_livro)
                novo_autor_livro.execute(sub_op)

        if opc == 3:
            print("1- Autor")
            print("2- Leitor")
            print("3- Livro")
            print("4- Autor do Livro\n")

            sub_op = input("Qual Entidade deseja remover: ")

            if sub_op == 1:
                cod = raw_input("De o codigo do autor que deseja remover: ")

                remove_autor = RemoverCommand(sub_op, cod)
                remove_autor.execute(sub_op)

            if sub_op == 2:
                cod = raw_input("De o codigo do leitor que deseja remover: ")

                remove_leitor = RemoverCommand(sub_op, cod)
                remove_leitor.execute(sub_op)

            if sub_op == 3:
                cod = raw_input("De o codigo do livro que deseja remover: ")

                remove_livro = RemoverCommand(sub_op, cod)
                remove_livro.execute(sub_op)

            if sub_op == 4:
                cod = raw_input("De o codigo do autor que deseja remover: ")

                remove_autor = RemoverCommand(sub_op, cod)
                remove_autor.execute(sub_op)

            print

        if opc == 4:
            print("1- Autor")
            print("2- Leitor")
            print("3- Livro")
            print("4- Autor do Livro\n")

            sub_op = input("Qual Entidade deseja visualizar: ")

            if sub_op == 1:

                mostrar_autor = MostrarCommand()
                mostrar_autor.execute(sub_op)

            if sub_op == 2:

                mostrar_leitor = MostrarCommand()
                mostrar_leitor.execute(sub_op)

            if sub_op == 3:

                mostrar_livro = MostrarCommand()
                mostrar_livro.execute(sub_op)

            if sub_op == 4:

                mostrar_autor_livro = MostrarCommand()
                mostrar_autor_livro.execute(sub_op)
