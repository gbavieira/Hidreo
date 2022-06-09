from django import forms
from basica.validation import *
from .models import LeadAvancada

class LeadAvancadaForms (forms.ModelForm):
    choices_modelo = [('On Grid', 'On Grid'),('Off Grid', 'Off Grid'),]
    choices_cabo = [('Alumínio', 'Alumínio'),('Cobre', 'Cobre'),]
    modelo = forms.ChoiceField(choices=choices_modelo, widget = forms.RadioSelect)
    tipo_cabo = forms.ChoiceField(choices=choices_cabo, widget = forms.RadioSelect)
    class Meta:
        model = LeadAvancada
        fields = '__all__'
        labels = {'desnivel':'Desnível (Queda) (m)','vazao':'Vazão (L/s)','dist_hidr':'Distância Hidráulica (Tubulação) (m)','dist_eletr':'Distância Elétrica (m)',}
        exclude = ['data']
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