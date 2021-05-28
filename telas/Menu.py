import os
import telas.AdicionarFrota
import telas.ListarFrotas
import telas.AtualizarFrota
import telas.ExcluirFrota
import telas.ReservarFrota
import telas.ProcurarReservas
import telas.AdicionarCliente
import telas.ListarClientes

def main():
  os.system("clear")
  print("|||||||||| Menu locadora G&G ||||||||||\n")
  print("01 - Adicionar frota")
  print("02 - Atualizar frota")
  print("03 - Excluir frota")
  print("04 - Listar frota(s)")
  print("05 - Reservar frota")
  print("06 - Atualizar reserva")
  print("07 - Cancelar reserva")
  print("08 - Procurar reserva(s)")
  print("09 - Adicionar cliente")
  print("10 - Atualizar cliente")  
  print("11 - Excluir cliente")
  print("12 - Listar cliente(s)")
  print("13 - Exportar json")
  print("14 - Importar json")
  print("15 - Sobre")
  print("16 - Sair\n")

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
    elif sel in ("8", "08"):
      telas.ProcurarReservas.main()
    elif sel in ("9", "09"):
      telas.AdicionarCliente.main()
    elif sel in ("12"):
      telas.ListarClientes.main()
  except Exception:
    print("Opção inválida")
  