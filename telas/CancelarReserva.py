import sqlite3
import telas.Menu
import telas.CancelarReserva
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Cancelamento de reserva:")
    seqreserva = int(input("Qual reserva deseja cancelar? "))
    if(conn.execute(f'select count(*) from reservas where seqreserva="{seqreserva}"').fetchone()[0] == 1):
      conn.execute(f'delete from reservas where seqreserva={seqreserva}') 
      conn.commit()
      input(f'Reserva {seqreserva} excluída com sucesso. Tecle Enter para voltar.')
      conn.close()
      telas.Menu.main()
    else:
      tenta = input("Reserva não encontrada, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.CancelarReserva.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao excluir, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.CancelarReserva.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()