import sqlite3
import telas.Menu
import telas.AdicionarFrota
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')

  print("Adicionar frota:")
  nomecarro = input("Digite o nome da frota: ")
  precodiaria = float(input("Digite o valor da diaria da frota: "))

  try:
    conn.execute(f'insert into frotas(nomefrota, precodiaria) values("{nomecarro}", "{precodiaria}")')
    conn.commit()
    input("Frota adicionada com sucesso. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()
  except:
    tenta = input("Erro ao adicionar frota, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.AdicionarFrota.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()



