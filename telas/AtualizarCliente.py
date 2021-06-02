import sqlite3
import telas.Menu
import telas.AtualizarCliente
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Atualização de cliente:")
    seqcliente = int(input("Qual cliente deseja atualizar? "))
    if(conn.execute(f'select count(*) from clientes where seqcliente="{seqcliente}"').fetchone()[0] == 1):
      print(f'Digite os novos dados para o cliente {seqcliente}')
      nomecliente = input("Digite o nome do cliente: ")
      conn.execute(f'update clientes set nomecliente="{nomecliente}" where seqcliente={seqcliente}') 
      conn.commit()
      input("Cliente atualizado com sucesso. Tecle Enter para voltar.")
      conn.close()
      telas.Menu.main()
    else:
      tenta = input("Cliente não cadastrado, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.AtualizarCliente.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao atualizar, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.AtualizarCliente.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()