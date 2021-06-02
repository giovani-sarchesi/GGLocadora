import sqlite3
import os
import json
import telas.Menu
from datetime import date
from shutil import make_archive

frotas = []
frota = {}
clientes = []
cliente = {}
reservas = []
reserva = {}
data = date.today().strftime('%d%m%Y')
os.system("clear")
conn = sqlite3.connect('./banco/dados.db')

def main():
  try:
    os.mkdir(f'./Arquivos_{data}')
    buscafrotas()
    buscaClientes()
    buscareservas()
    zipar()
  except:
    print("Erro ao gerar arquivos.")

def buscafrotas():
  frotasbanco = conn.execute(f'select * from frotas').fetchall()
  for fb in frotasbanco:
    frota.clear
    frota['seqfrota'] = fb[0]
    frota['nomefrota'] = fb[1]
    frota['precodiaria'] = fb[2]

    frotas.append(frota.copy())
  
  exportar('Frotas', frotas)

def buscareservas():
  reservasbanco = conn.execute(f'SELECT a.seqreserva, a.seqcliente,c.nomecliente, a.seqfrota, b.nomefrota, a.qtdediarias, a.vlrreserva FROM reservas a, frotas b, clientes c WHERE a.seqcliente = c.seqcliente AND a.seqfrota = b.seqfrota ORDER BY a.seqreserva').fetchall()
  for rb in reservasbanco:
    reserva.clear
    reserva['seqreserva'] = rb[0]
    reserva['seqcliente'] = rb[1]
    reserva['nomecliente'] = rb[2]
    reserva['seqfrota'] = rb[3]
    reserva['nomefrota'] = rb[4]
    reserva['qtdediarias'] = rb[5]
    reserva['vlrreserva'] = rb[6]

    reservas.append(reserva.copy())
  
  exportar('Reservas', reservas)

def buscaClientes():
  clientesbanco = conn.execute(f'select * from clientes').fetchall()
  for cb in clientesbanco:
    cliente.clear
    cliente['seqcliente'] = cb[0]
    cliente['nomecliente'] = cb[1]

    clientes.append(cliente.copy())
  
  exportar('Clientes', clientes)

def exportar(arquivo, dados):
  with open(f'./Arquivos_{data}/{arquivo}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

def zipar():
  make_archive(f'Arquivos_{data}', 'zip', './', f'ArquivosZippados_{data}')

