import sqlite3
import telas.Menu
import telas.ExcluirFrota
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Atualização de frota:")
    seqfrota = int(input("Qual frota deseja excluir? "))
    if(conn.execute(f'select count(*) from frotas where seqfrota="{seqfrota}"').fetchone()[0] == 1 and conn.execute(f'select count(*)from reservas where seqfrota={seqfrota}').fetchone()[0] == 0):
      conn.execute(f'delete from frotas where seqfrota={seqfrota}') 
      conn.commit()
      input(f'Frota {seqfrota} excluída com sucesso. Tecle Enter para voltar.')
      conn.close()
      telas.Menu.main()
    else:
      tenta = input("Frota não encontrada ou existe reservas vinculadas a mesma, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.ExcluirFrota.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao excluir, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.ExcluirFrota.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()
    