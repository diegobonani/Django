from django import forms
from .models import CadastroPessoas

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrarForms(forms.ModelForm):
    '''
    nome = models.CharField(max_length=50),
    sobrenome = models.CharField(max_length=50),
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    email = models.EmailField(),
    apelido = models.CharField(max_length=40)
    observacao = models.TextField()
    '''

    class Meta:
        model = CadastroPessoas

        fields = ('nome', 'sobrenome', 'idade', 'data_nascimento', 'email', 'apelido', 'observacao')





