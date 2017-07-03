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

            print(self._cod)

            if self._cod in autor_db:
                print ("Codigo ja existente, por favor, tente novamente.\n")
                return

            autor_db[self._cod] = self._nome

            print (autor_db[self._cod])
            print (autor_db.keys())
            print (autor_db.values())
            print

            autor_db.close()

        if op == 2:
            leitor_db = bsddb.btopen('leitor.db', 'c')

            print(self._cod)

            if self._cod in leitor_db:
                print ("Codigo ja existente, por favor, tente novamente.\n")
                return

            leitor_db[self._cod] = self._nome

            print (leitor_db[self._cod])
            print (leitor_db.keys())
            print (leitor_db.values())
            print

            leitor_db.close()

        if op == 3:
            livros_db = bsddb.btopen('livros.db', 'c')

            print(self._cod)

            if self._cod in livros_db:
                print ("Codigo ja existente, por favor, tente novamente.\n")
                return

            livros_db[self._cod] = self._nome

            print (livros_db[self._cod])
            print (livros_db.keys())
            print (livros_db.values())
            print

            livros_db.close()

        if op == 4:
            livros_db = bsddb.btopen('livros.db', 'r')
            autor_db = bsddb.btopen('autor.db', 'r')
            autor_livro_db = bsddb.btopen('autor_livro.db', 'c')


            if (self._codL in livros_db) and (self._codA in autor_db):

                autor_livro_db[self._codL] = self._codA

            else:
                print ("Codigo do livro ou autor invalido.\n")
                return

            print ("O livro %s foi escrito pelo autor(a): %s\n" %(livros_db[self._codL],autor_db[self._codA]))

            autor_livro_db.close()
            livros_db.close()
            autor_db.close()