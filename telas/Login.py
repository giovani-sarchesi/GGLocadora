import os
import telas.Menu
import telas.Login

def main():
  os.system("clear")
  try:
    print("|||||||||||🚗  Locadora de carros G&G 🚗 |||||||||||")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario not in ('admin') and senha not in ('admin'):
      print("Usuário ou senha incorretos, tecle Enter para tentar novamente.")
      telas.Login.main()
    else:
      telas.Menu.main()
  except Exception:
    print(Exception)

