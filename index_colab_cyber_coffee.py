!pip install -u -q google-generativeai

#importacoes e configuracoes iniciais

import numpy as np
import google.generativeai as genai

from IPython.display import Image

GOOGLE_API_KEY="sua API KEY"
genai.configure(api_key=GOOGLE_API_KEY)



#Array de cafés

sabores = np.array([
    {
        "nome": "Café Expresso",
        "ingredientes": "Café moído e água",
        "preco": 5.00,
        "caminho_imagem": "./coffe-expresso.jpeg"
    },
    {
        "nome": "Café com Leite",
        "ingredientes": "Café expresso e leite",
        "preco": 7.00,
        "caminho_imagem": "./cafe-com-leite.jpeg"
    },
    {
        "nome": "Cappuccino",
        "ingredientes": "Café expresso, leite e espuma de leite",
        "preco": 10.00,
        "caminho_imagem": "./cappuccino.jpeg"
    },
    {
        "nome": "Mocha",
        "ingredientes": "Café expresso, leite, chocolate e chantilly",
        "preco": 12.00,
        "caminho_imagem": "./mocha.jpeg"
    }
])

def validar_item(item, cardapio):
  for itemCardapio in cardapio:
            if itemCardapio["nome"] == item:
                print(f' Ótima escolha, saindo um {itemCardapio["nome"]} no capricho!')
                gerar_imagem(itemCardapio["caminho_imagem"])  
                return True
  
  return False



def reescrever_texto_informal(texto):
    prompt = f"Reescreva esse texto de forma mais fluída, sem sai do contexto de venda de café, quebre linha se for preciso e seguindo o medelo: {texto} "

    model_2 = genai.GenerativeModel("gemini-1.0-pro",
                                  generation_config=generation_config)
    
    resposta = model_2.generate_content(prompt)

    return resposta.text


def gerar_imagem(caminho_imagem):
  imagem = Image(filename=caminho_imagem)
  display(imagem)



# Função para processar o pedido do cliente
def processar_pedido(sabores):
    # Inicie um loop para interagir com o cliente
    while True:
        # Obtenha a entrada do cliente
        inicio_conversa = "Olá, sou a Márcia do CyberCoffe, gostaria de um café? Esse é o nosso cardápio:\n"

        for sabor in sabores:
          inicio_conversa += f"- {sabor['nome']} - R$ {sabor['preco']}\n"

        inicio_conversa += "Que sabor vai querer?"


        texto_informal = reescrever_texto_informal(inicio_conversa)

        escolha = input(texto_informal)

        # Encontre o produto escolhido no array
        if not escolha:
          print("\n\n-----------------------------------------------------------")
          print("Escolha vazia. Por favor, escolha um item do cardápio.")
          print("-----------------------------------------------------------\n\n")
          
          continue

        if not validar_item(escolha, sabores):
          print("\n\n-----------------------------------------------------------")
          print(f"O item '{escolha}' não está no cardápio. Por favor, escolha um item válido.")
          print("-----------------------------------------------------------\n\n")
          continue

        break


processar_pedido(sabores)



