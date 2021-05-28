import os
import telas.AdicionarFrota
import telas.ListarFrotas

def main():
  os.system("clear")
  print("|||||||||| Menu locadora G&G ||||||||||\n")
  print("01 - Adicionar frota")
  print("02 - Atualizar frota")
  print("03 - Excluir frota")
  print("04 - Listar frota(s)")
  print("05 - Criar reserva")
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
    elif sel in ("4", "04"):
      telas.ListarFrotas.main()
  except Exception:
    print("Opção inválida")
  