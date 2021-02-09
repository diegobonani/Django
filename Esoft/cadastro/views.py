from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import CadastroPessoas
from .forms import RegistrarForms
import requests

def pessoasCadastradas(request):
    data = CadastroPessoas.objects.all()
    return render(request, 'pessoasCadastradas.html', {'data': data})

def paginaInicial(request):
    api = requests.get('https://gerador-nomes.herokuapp.com/nome/aleatorio')
    gereNome = api.json()
    form = RegistrarForms(request.POST or None)
    form.fields["nome"].initial = gereNome[0] + " " + gereNome[1]
    form.fields['sobrenome'].initial = gereNome[2]
    if form.is_valid():
        try:
            form.save()
            return redirect('pessoasCadastradas')
        except:
            pass
    return render(request, 'formulario.html', {'form': form})

def update_pessoas(request,id):
    data = {}
    cadastrao = CadastroPessoas.objects.get(id=id)
    form = RegistrarForms(request.POST or None, instance=cadastrao)
    if form.is_valid():
        form.save()
        return redirect('pessoasCadastradas')
    return render(request, 'pessoasCadastradas.html', {'form':form , 'data':data})

def deletar_pessoas(request,id):
    cadastrao = CadastroPessoas.objects.get(id=id)
    cadastrao.delete()
    return redirect('pessoasCadastradas')



'''
def registar(request):
    if request.method == 'POST':
        form = CadastroPessoas(request.POST)

        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('/pessoas/')

    else:
        form = RegisterForm()

    return render(request, 'formulario.html', {'register_form': form})


def pessoas_registradas(request):
    registers = CadastroPessoas.objects.all()

    if request.method == 'POST':
        form = FilterForm(request.POST or None)

        if form.is_valid():

            context = {
                'nome': request.POST['nome'],
                'sobrenome': request.POST['sobrenome'],
                'city': request.POST['city'],
            }

            if context['idade']:
                age_choosed = re.sub("[''{ birthday: datetime.date()}]", '', context['age'])
                age_choosed = re.sub('[,]', '-', age_choosed)

                registers = CadastroPessoas.objects.filter(birthday=age_choosed)

            elif context['city']:
                registers = CadastroPessoas.objects.filter(city=form.cleaned_data.get('city'))

            elif request.POST['gender']:
                registers = CadastroPessoas.objects.filter(gender=form.cleaned_data.get('gender'))

    else:
        form = FilterForm()

    return render(request, 'pessoasCadastradas.html', {'registers': registers, 'form_filter': form})
'''