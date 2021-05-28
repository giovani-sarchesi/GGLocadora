import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')

  print("Adicionar frota:")
  nomecarro = input("Digite o nome da frota: ")
  ano = int(input("Digite o ano da frota: "))
  km = input("Digite quantidade km da frota: ")
  precodiaria = input("Digite o valor da diaria da frota: ")


  try:
    conn.execute(f'insert into frotas(nomefrota, ano, qtdkm, precodiaria) values("{nomecarro}", "{ano}", "{km}", "{precodiaria}")')
    conn.commit()
    input("Frota adicionada com sucesso. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao adicionar a frota. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()



