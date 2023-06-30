from django.shortcuts import render

def view_home(request):
    return render(request, 'fender/paginas/index.html')

def view_produto(request):
    return render(request, 'fender/paginas/produto.html')