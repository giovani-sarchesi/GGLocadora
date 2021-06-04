import sqlite3
import telas.Menu
import telas.ReservarFrota
import os

def main():
  os.system("clear")
  conn = sqlite3.connect('./banco/dados.db')
  
  try:
    print("Reserva de frota:")
    seqfrota = int(input("Qual frota deseja reservar? "))
    frota = conn.execute(f'select * from frotas where seqfrota="{seqfrota}"').fetchall()
    if(frota != []):
      seqcliente = int(input("Qual cliente irá reservar? "))
      cliente = conn.execute(f'select * from clientes where seqcliente="{seqcliente}"').fetchall()
      if(cliente != []):
        qtddiarias = float(input("Quantas diárias deseja reservar? "))
        if qtddiarias <= 0:
          tenta = input("A quantidade de diárias deve ser maior que 0, deseja tentar novamente? S - Sim / N - Não ")
          if tenta in ('S', 's', 'Sim', 'sim'):
            telas.ReservarFrota.main()
          elif tenta in ('N', 'n', 'Não', 'não'):
            conn.close()
            telas.Menu.main()
        else:
          for f in frota:
            for c in cliente:
              confirma = input(f'Confirmar reserva?\nFrota: {f[0]} - {f[1]}\nCliente: {c[0]} - {c[1]}\nDiárias: {qtddiarias}\nValor total: {f[2] * qtddiarias}?\nS - Sim / N - Não\n')
              if confirma in ('S', 's', 'Sim', 'sim'):
                conn.execute(f'insert into reservas(seqfrota, seqcliente, qtdediarias, vlrreserva) values("{f[0]}", "{c[0]}", "{qtddiarias}", "{qtddiarias * f[2]}")')
                conn.commit()
                input("Reserva realizada com sucesso. Tecle Enter para voltar.")
                conn.close()
                telas.Menu.main()
              else:
                conn.close()
                telas.Menu.main()        
      else:
        tenta = input("Cliente não encontrado, deseja tentar novamente? S - Sim / N - Não ")
        if tenta in ('S', 's', 'Sim', 'sim'):
          telas.ReservarFrota.main()
        elif tenta in ('N', 'n', 'Não', 'não'):
          conn.close()
          telas.Menu.main()
    else:
      tenta = input("Frota não encontrada, deseja tentar novamente? S - Sim / N - Não ")
      if tenta in ('S', 's', 'Sim', 'sim'):
        telas.ReservarFrota.main()
      elif tenta in ('N', 'n', 'Não', 'não'):
        conn.close()
        telas.Menu.main()
  except:
    tenta = input("Erro ao reservar frota, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.ReservarFrota.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      conn.close()
      telas.Menu.main()
    