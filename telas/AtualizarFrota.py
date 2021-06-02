import sqlite3
import telas.Menu
import telas.AtualizarFrota
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Atualização de frota:")
    seqfrota = int(input("Qual frota deseja atualizar? "))
    if(conn.execute(f'select count(*) from frotas where seqfrota="{seqfrota}"').fetchone()[0] == 1):
      print(f'Digite os novos dados para a frota {seqfrota}')
      nomecarro = input("Digite o nome da frota: ")
      precodiaria = input("Digite o valor da diaria da frota: ")
      conn.execute(f'update frotas set nomefrota="{nomecarro}", precodiaria="{precodiaria}" where seqfrota={seqfrota}') 
      conn.commit()
      input("Frota atualizada com sucesso. Tecle Enter para voltar.")
      conn.close()
      telas.Menu.main()
    else:
      tenta = input("Frota não cadastrada, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.AtualizarFrota.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao atualizar, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.AtualizarFrota.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()
    