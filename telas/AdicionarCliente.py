import sqlite3
import telas.Menu
import telas.AdicionarCliente
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')

  print("Adicionar cliente:")
  nomecliente = input("Digite o nome do cliente: ")

  try:
    conn.execute(f'insert into clientes(nomecliente) values("{nomecliente}")')
    conn.commit()
    input("Cliente adicionado com sucesso. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()
  except:
    tenta = input("Erro ao adicionar cliente, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.AdicionarCliente.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()



