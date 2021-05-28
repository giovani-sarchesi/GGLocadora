import telas.Login
import telas.Menu
import banco.tabelas as banco

banco.create()
logado = telas.Login.main()

if logado:
  telas.Menu.main()
else:
  print("Usuário ou senha incorreto.")
