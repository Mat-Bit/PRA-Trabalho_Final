import bsddb
from MenuCommand import *

class RemoverCommand(MenuCommand):

    def __init__(self, op, cod):
        if op == 1:
            self._cod = cod

        if op == 2:
            self._cod = cod

        if op == 3:
            self._cod = cod

        if op == 4:
            self._codL = cod


    def execute(self, op):
        if op == 1:
            autor_db = bsddb.btopen('autor.db', 'c')

            if self._cod not in autor_db:
                print ("Codigo nao existente, por favor, tente novamente.\n")
                return

            autor_db.pop(self._cod)

            autor_db.close()

        if op == 2:
            leitor_db = bsddb.btopen('leitor.db', 'c')

            if self._cod not in leitor_db:
                print ("Codigo nao existente, por favor, tente novamente.\n")
                return

            leitor_db.pop(self._cod)

            leitor_db.close()

        if op == 3:
            livros_db = bsddb.btopen('livros.db', 'c')

            print(self._cod)

            if self._cod not in livros_db:
                print ("Codigo nao existente, por favor, tente novamente.\n")
                return

            livros_db.pop(self._cod)


            livros_db.close()

        if op == 4:
            autor_livro_db = bsddb.btopen('autor_livro.db', 'c')


            if (self._codL in autor_livro_db):

                autor_livro_db.pop(self._codL)

            else:
                print ("Codigo do livro invalido.\n")
                return

            autor_livro_db.close()

