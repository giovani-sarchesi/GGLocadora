import sqlite3
import os
import json
import telas.Menu
import telas.Exportarjson
from datetime import date
import zipfile

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
    os.system("clear")
    print("Gerando arquivo de Frotas...")
    buscafrotas()
    print("Frotas exportadas.")
    print("Gerando arquivo de Clientes...")
    buscaClientes()
    print("Clientes exportados.")
    print("Gerando arquivo de Reservas...")
    buscareservas()
    print("Reservas exportadas.")
    input("Consulte os arquivos na pasta Exportados. Tecle Enter para continuar.")
    telas.Menu.main()
    conn.close()
    #zipar()
  except:
    tenta = input("Erro ao gerar arquivo(s), deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.Exportarjson.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()

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
  with open(f'./Exportados/{arquivo}_{data}.json', 'w') as json_file:
        json.dump(dados, json_file, indent=4)

def zipar():
  path_zip = os.path.join(os.sep, os.getcwd(), f'Exportados\Arquivos_{data}.zip')
  path_dir = os.path.join(os.sep, os.getcwd().replace("telas", ''), f"Arquivos_{data}")

  zf = zip.ZipFile(path_zip, "w")
  for dirname, subdirs, files in os.walk(path_dir):
    for filename in files:
      if(filename.endswith('.json')):
        zf.write(os.path.join(dirname, filename))
        os.remove(os.path.join(dirname, filename))
  
  zf.close()