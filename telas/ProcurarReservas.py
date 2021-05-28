import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  cursor = conn.cursor()

  print("Reserva(s):")


  try:
    cursor.execute("""SELECT * FROM reservas;""")

    for linha in cursor.fetchall():
      print(linha)

    input("Tecle Enter para voltar...")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao buscar reservas. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()