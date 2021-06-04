import os
import requests
import json
import telas.Importarjson
import telas.Menu
import sqlite3

urlmarcas = 'http://fipeapi.appspot.com/api/1/carros/marcas.json'
urlveiculos = 'http://fipeapi.appspot.com/api/1/carros/veiculos/{}.json'
urlmodelos = 'http://fipeapi.appspot.com/api/1/carros/veiculo/{}/{}.json'
urlfinal = 'http://fipeapi.appspot.com/api/1/carros/veiculo/{}/{}/{}.json'
def main():
  try:
    os.system("clear")
    requisicao = requests.get(urlmarcas)
    marcas = json.loads(requisicao.content)

    print("Marcas:")
    for marca in marcas:
      print('{} - {}'.format(marca['id'], marca['name']))

    veiculo = int(input("Digite o código da marca que deseja selecionar: "))
    requisicao = requests.get(urlveiculos.format(veiculo))
    veiculos = json.loads(requisicao.content)
    
    os.system("clear")
    print("Veículos:")
    for vei in veiculos:
      print('{} - {}'.format(vei['id'], vei['name']))

    modelo = int(input("Digite o código do modelo que deseja selecionar: "))
    requisicao = requests.get(urlmodelos.format(veiculo, modelo))
    modelos = json.loads(requisicao.content)

    os.system("clear")
    print("Modelos:")
    for mod in modelos:
      print('{} - {}'.format(mod['id'], mod['veiculo']))

    final = input("Digite o código do veículo que deseja selecionar: ")
    requisicao = requests.get(urlfinal.format(veiculo, modelo, final))
    final = json.loads(requisicao.content)

    os.system("clear")
    print("Veículo:")
    nomecarro = (final['name'])
    precodiaria = final['preco'].replace("R$ ", "")
    precodiaria = precodiaria.replace(".", "")
    precodiaria = precodiaria.replace(",", ".")
    precodiaria = (round(float(precodiaria)/500.00, 2))
    conn = sqlite3.connect('./banco/dados.db')
    conn.execute(f'insert into frotas(nomefrota, precodiaria) values("{nomecarro}", "{precodiaria}")')
    conn.commit()
    input("Frota {} com o preço de diária R${} importada com sucesso. Tecle Enter para voltar.".format(nomecarro, precodiaria))
    conn.close()
    telas.Menu.main()

    
  except:
    os.system("clear")
    tenta = input("Erro ao consumir dados, deseja tentar novamente? S - Sim / N - Não ")
    if tenta in ('S', 's', 'Sim', 'sim'):
      telas.Importarjson.main()
    elif tenta in ('N', 'n', 'Não', 'não'):
      telas.Menu.main()
  