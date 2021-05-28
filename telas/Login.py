import os

def main():
  os.system("clear")
  try:
    print("|||||||||||🚗  Locadora de carros G&G 🚗 |||||||||||")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario not in ('admin') and senha not in ('admin'):
      return False
    else:
      return True
  except Exception:
    print(Exception)

