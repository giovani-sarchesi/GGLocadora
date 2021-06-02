import sqlite3
import telas.Menu
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')

  print("Reserva(s):")


  try:
    reservas = conn.execute("""SELECT a.seqreserva, c.nomecliente, b.nomefrota, a.qtdediarias, a.vlrreserva FROM reservas a, frotas b, clientes c WHERE a.seqcliente = c.seqcliente AND a.seqfrota = b.seqfrota ORDER BY a.seqreserva;""").fetchall()

    for reserva in reservas:
      print("_______________________________________")
      print(f'Reserva código: {reserva[0]}')
      print(f'Cliente: {reserva[1]}')
      print(f'Frota: {reserva[2]}')
      print(f'Diárias: {reserva[3]}')
      print(f'Valor total reserva: R${reserva[4]}')
      print("_______________________________________")

    input("Tecle Enter para voltar...")
    conn.close()
    telas.Menu.main()
  except:
    input("Erro ao buscar reservas. Tecle Enter para voltar.")
    conn.close()
    telas.Menu.main()