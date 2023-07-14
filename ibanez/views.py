from django.shortcuts import render
from . import models

def view_home(request):
    return render(request, 'ibanez/paginas/index.html')

def view_produto(request, id):
    resultado = models.Tipo.objects.get(id = id)
    return render(request, 'ibanez/paginas/produto.html', context={'dicionario':resultado}
                  )

def view_produtos(request):
    produtos = []
    tipos = models.Tipo.objects.filter(emEstoque = True)
    for i in tipos:
        produtos.append(i.__dict__)
    return render(request, 'ibanez/paginas/produtos.html', context={'dicionario':produtos}
                  )