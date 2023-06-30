from django.shortcuts import render

def view_home(request):
    return render(request, 'gibson/paginas/index.html')

def view_produto(request):
    return render(request, 'gibson/paginas/produto.html')