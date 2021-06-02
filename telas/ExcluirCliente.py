import sqlite3
import telas.Menu
import telas.ExcluirCliente
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Exclusão de cliente:")
    seqcliente = int(input("Qual cliente deseja excluir? "))
    if(conn.execute(f'select count(*) from clientes where seqcliente="{seqcliente}"').fetchone()[0] == 1 and conn.execute(f'select count(*)from reservas where seqcliente={seqcliente}').fetchone()[0] == 0):
      conn.execute(f'delete from clientes where seqcliente={seqcliente}') 
      conn.commit()
      input(f'Cliente {seqcliente} excluído com sucesso. Tecle Enter para voltar.')
      conn.close()
      telas.Menu.main()
    else:
      tenta = input("Cliente não cadastrado ou possui reservas em seu nome, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.ExcluirCliente.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao excluir, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.ExcluirCliente.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()