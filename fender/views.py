from django.shortcuts import render
from . import models

def view_home(request):
    return render(request, 'fender/paginas/index.html')

def view_produto(request, id):
    resultado = models.TipoFender.objects.get(id = id)
    resultado = resultado.__dict__
    print(resultado)
    return render(request, 'fender/paginas/produto.html', context=resultado
                  )

def view_produtos(request):
    produtos = []
    tipos = models.TipoFender.objects.filter(emEstoque = True)
    for i in tipos:
        produtos.append(i.__dict__)
    return render(request, 'fender/paginas/produtos.html', context={'dicionario':produtos}
                  )