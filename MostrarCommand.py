import bsddb
from MenuCommand import *

class MostrarCommand(MenuCommand):


    def execute(self, op):
        if op == 1:
            autor_db = bsddb.btopen('autor.db', 'r')

            for k, v in autor_db.iteritems():
                print "Codigo: %s\tAutor: %s" %(k, v)
            print

            autor_db.close()

        if op == 2:
            leitor_db = bsddb.btopen('leitor.db', 'r')

            for k, v in leitor_db.iteritems():
                print "Codigo: %s\tLeitor: %s" % (k, v)
            print

            leitor_db.close()

        if op == 3:
            livros_db = bsddb.btopen('livros.db', 'r')

            for k, v in livros_db.iteritems():
                print "Codigo: %s\tLivro: %s" % (k, v)
            print

            livros_db.close()

        if op == 4:
            livros_db = bsddb.btopen('livros.db', 'r')
            autor_db = bsddb.btopen('autor.db', 'r')
            autor_livro_db = bsddb.btopen('autor_livro.db', 'r')


            for k, v in autor_livro_db.iteritems():
                if (k in livros_db) and (v in autor_db):
                    print ("O livro %s foi escrito pelo autor(a): %s" % (livros_db[k], autor_db[v]))
            print

            autor_livro_db.close()
            livros_db.close()
            autor_db.close()