from django.shortcuts import render

PRODUTOS = [
    {'tipo':1, 'nome':'TOD10N', 'descricao':'Tim Henson electric signature guitar', 'emEstoque':True},
    {'tipo':2, 'nome':'ICHI00', 'descricao':'Ichika Nito electric signature guitar', 'emEstoque':True},
    {'tipo':3, 'nome':'PIA77', 'descricao':'Steve Vai electric signature guitar', 'emEstoque':True},
    {'tipo':4, 'nome':'KIKO100', 'descricao':'Kiko Loureiro electric signature guitar', 'emEstoque':True},
    {'tipo':5, 'nome':'KRYS10', 'descricao':'Scott LePage electric signature guitar', 'emEstoque':True},
]

def view_home(request):
    return render(request, 'ibanez/paginas/index.html')

def view_produto(request, id):
    resultado = {}
    for item in PRODUTOS:
        if item['tipo'] == id:
            resultado = item
            break
    return render(request, 'ibanez/paginas/produto.html', context=resultado)

def view_produtos(request):
    dicionario = {'tipos' : PRODUTOS}
    return render(request, 'ibanez/paginas/produtos.html', context=dicionario)