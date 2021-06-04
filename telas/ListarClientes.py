import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  cursor = conn.cursor()

  print("Cliente(s) cadastrado(s):")


  try:
    cursor.execute("""SELECT * FROM clientes;""")

    for linha in cursor.fetchall():
      print("=====================================")
      print(f'Código: {linha[0]}')
      print(f'Nome cliente: {linha[1]}')
      print("=====================================")

    input("Tecle Enter para voltar...")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao buscar clientes. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()