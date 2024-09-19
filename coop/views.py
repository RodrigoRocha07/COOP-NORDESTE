from django.shortcuts import render
from coop.models import *


def mostrar_home(request):
    cooperados = Cooperado.objects.all()
    return render (request,"home.html",{'cooperados':cooperados})


def mostrar_sobre(request):
    return render (request,"sobre.html")




def mostrar_cadastro(request):
    return render (request,"cadastro.html")



def cadastrar(request):

    nome = request.POST.get('nome')
    cpf_cnpj = request.POST.get('cpf_cnpj')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    ativo = request.POST.get('ativo') == 'on'  


    Cooperado.objects.create(
        nome=nome,
        cpf_cnpj=cpf_cnpj,
        endereco=endereco,
        telefone=telefone,
        ativo=ativo
    )


    return render(request, 'cadastro.html')






def mostrar_contato(request):
    return render (request,"contato.html")


