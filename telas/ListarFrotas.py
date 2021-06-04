import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  cursor = conn.cursor()

  print("Frota(s) cadastrada(s):")


  try:
    cursor.execute("""SELECT * FROM frotas;""")

    for linha in cursor.fetchall():
      print("=============================================")
      print(f'Código: {linha[0]}')
      print(f'Nome carro: {linha[1]}')
      print(f'Preço diária: R${linha[2]}')
      print("=============================================")

    input("Tecle Enter para voltar...")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao buscar frotas. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()