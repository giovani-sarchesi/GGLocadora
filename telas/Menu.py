import os
import telas.Login
import telas.AdicionarFrota
import telas.ListarFrotas
import telas.AtualizarFrota
import telas.ExcluirFrota
import telas.ReservarFrota
import telas.CancelarReserva
import telas.ProcurarReservas
import telas.AdicionarCliente
import telas.AtualizarCliente
import telas.ExcluirCliente
import telas.ListarClientes
import telas.Exportarjson
import telas.Sobre

def main():
  os.system("clear")
  print("|||||||||| Menu locadora G&G ||||||||||\n")
  print("01 - Adicionar frota")
  print("02 - Atualizar frota")
  print("03 - Excluir frota")
  print("04 - Listar frota(s)")
  print("05 - Reservar frota")
  print("06 - Cancelar reserva")
  print("07 - Procurar reserva(s)")
  print("08 - Adicionar cliente")
  print("09 - Atualizar cliente")  
  print("10 - Excluir cliente")
  print("11 - Listar cliente(s)")
  print("12 - Exportar json")
  print("13 - Importar json")
  print("14 - Sobre")
  print("15 - Sair\n")

  try:
    sel = input("Selecione a opção que deseja: ")

    if sel in ("1", "01"):
      telas.AdicionarFrota.main()
    elif sel in ("2", "02"):
      telas.AtualizarFrota.main()
    elif sel in ("3", "03"):
      telas.ExcluirFrota.main()
    elif sel in ("4", "04"):
      telas.ListarFrotas.main()
    elif sel in ("5", "05"):
      telas.ReservarFrota.main()
    elif sel in ("6", "06"):
      telas.CancelarReserva.main()
    elif sel in ("7", "07"):
      telas.ProcurarReservas.main()
    elif sel in ("8", "08"):
      telas.AdicionarCliente.main()
    elif sel in ("9", "09"):
      telas.AtualizarCliente.main()  
    elif sel in ("10"):
      telas.ExcluirCliente.main()  
    elif sel in ("11"):
      telas.ListarClientes.main()
    elif sel in ("12"):
      telas.Exportarjson.main()
    elif sel in ("14"):
      telas.Sobre.main()
    elif sel in ("15"):
      input("Obrigado por utilizar nosso sistema, tecle Enter para finalizar.")
      telas.Login.main()

  except Exception:
    print("Opção inválida, tecle Enter para recarregar.")
    telas.Menu.main()
  