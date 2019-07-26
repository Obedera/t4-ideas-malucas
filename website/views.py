from django.shortcuts import render
from website.models import Pessoa
from website.models import Ideia

# Create your views here.

def index(request):
    # essa pagina é de cadastro
    args = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        return(request, 'login',{})

    return render(request, 'index.html', args)

def sobre(request):
    pessoa = Pessoa.objects.filter(ativo=True).all()
    args = {
        'pessoa':pessoa
    }
    return render(request, 'sobre.html', args)

def login(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa_bd = Pessoa.objects.filter(email=email_form).first()

        if pessoa_bd is None:
            contexto = {'msg':'Cadastre-se aqui'}
            return render(request,'index.html',contexto)
        else:
            contexto = {'pessoa': pessoa_bd}
            return render(request,'ideias.html',contexto)

        

    return render(request, 'login.html',{})


def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa
    return render(request,'ideias.html',{})


