from django import forms
from .validation import *
from .models import LeadBasica

class LeadBasicaForms (forms.ModelForm):
    class Meta:
        model = LeadBasica
        fields = '__all__'
        labels = {}
        widgets = {
            'potencia': forms.HiddenInput(),
            'mchs': forms.HiddenInput(),
        }

    def clean(self):
        nome = self.cleaned_data.get('nome')
        lista_de_erros = {}
        campo_tem_algum_numero(nome, 'nome', lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data