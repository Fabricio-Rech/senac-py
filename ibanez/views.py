from django.shortcuts import render
from . import models

def view_home(request):
    return render(request, 'ibanez/paginas/index.html')

def view_produto(request, id):
    # resultado = {}
    # PRODUTOS =
    # for item in PRODUTOS:
    #     if item['tipo'] == id:
    #         resultado = item
    #         break
    return render(request, 'ibanez/paginas/produto.html', #context=resultado
                  )

def view_produtos(request):
    
    PRODUTOS = models.tipo.object.all()
    print(PRODUTOS)
    # dicionario = {'tipos' : PRODUTOS}
    return render(request, 'ibanez/paginas/produtos.html', # context=dicionario
                  )