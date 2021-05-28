import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  cursor = conn.cursor()

  print("Frotas cadastradas:")


  try:
    cursor.execute("""SELECT * FROM frotas;""")

    for linha in cursor.fetchall():
      print(linha)

    input("Tecle Enter para voltar...")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao buscar frotas. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()