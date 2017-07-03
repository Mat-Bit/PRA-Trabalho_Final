import bsddb
from MenuCommand import *

class EditaCommand(MenuCommand):

    def __init__(self, op, objeto):
        if op == 1:
            self._nome = objeto.getNome()
            self._cod = objeto.getCod()

        if op == 2:
            self._nome = objeto.getNome()
            self._cod = objeto.getCod()

        if op == 3:
            self._nome = objeto.getNome()
            self._cod = objeto.getCod()

        if op == 4:
            self._codL = objeto.getCodL()
            self._codA = objeto.getCodA()

    def execute(self, op):
        if op == 1:
            autor_db = bsddb.btopen('autor.db', 'c')

            if self._cod in autor_db:
                autor_db[self._cod] = self._nome

                print (self._cod)
                print (autor_db[self._cod])
                print

            else:
                print ("Codigo invalido, por favor, tente novamente.\n")

            autor_db.close()

        if op == 2:
            leitor_db = bsddb.btopen('leitor.db', 'c')

            if self._cod in leitor_db:
                leitor_db[self._cod] = self._nome

                print (self._cod)
                print (leitor_db[self._cod])
                print

            else:
                print ("Codigo invalido, por favor, tente novamente.\n")

            leitor_db.close()

        if op == 3:
            livros_db = bsddb.btopen('livros.db', 'c')

            if self._cod in livros_db:
                livros_db[self._cod] = self._nome

                print (self._cod)
                print (livros_db[self._cod])
                print

            else:
                print ("Codigo invalido, por favor, tente novamente.\n")

            livros_db.close()

        if op == 4:
            livros_db = bsddb.btopen('livros.db', 'r')
            autor_db = bsddb.btopen('autor.db', 'r')
            autor_livro_db = bsddb.btopen('autor_livro.db', 'c')


            if (self._codL in livros_db) and (self._codA in autor_db):
                autor_livro_db[self._codL] = self._codA

                print (self._codL)
                print (autor_livro_db[self._codL])
                print

            else:
                print ("Codigo do livro ou autor invalido.\n")


            autor_livro_db.close()
            livros_db.close()
            autor_db.close()