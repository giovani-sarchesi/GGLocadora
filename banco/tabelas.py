import os
import sqlite3

def create():
    os.system("clear")
    exist = False

    if os.path.isfile('./banco/dados.db'):
        exist = True

    if (exist == False):
        con = sqlite3.connect('./banco/dados.db')
        con.execute("""
        create table if not exists frotas(
                seqfrota integer not null primary key autoincrement,
                nomefrota text not null,
                ano integer not null,
                qtdkm text not null,
                precodiaria text not null
            );""")

        con.execute("""
        create table if not exists reservas(
                seqreserva integer not null primary key autoincrement,
                seqfrota integer not null,
                seqcliente integer not null,
                qtdediarias text not null,
                vlrreserva text not null,

                foreign key(seqfrota) references frotas(seqfrota)
                foreign key(seqcliente) references clientes(seqcliente)
            );
            """)

        con.execute("""
        create table if not exists clientes(
                seqcliente integer not null primary key,
                nomecliente text not null
            );
            """)

        con.commit()
        print("Banco de dados criado com sucesso !")
        input("Tecle entrar para continuar..")

    else:
        print("O Banco de dados já está criado !")
        input("Tecle entrar para continuar..")