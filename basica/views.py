from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import LeadBasica
import math

def index(request):
    return render(request,'index.html')

def basica(request,desnivel=0,vazao=0):
    if request.method == 'POST':
        nome = request.POST['nome']
        desnivel = math.floor(int(float(request.POST['desnivel'])))
        vazao = math.floor(int(float(request.POST['vazao'])))
        potencia = math.ceil(desnivel*vazao*9.81*0.531)
        if potencia <= 75000:
            mchs = potencia/1000
            if potencia%1000 >= 500:
                mchs = math.ceil(mchs)
            else:
                mchs = math.floor(mchs)
        else:
            messages.error(request, 'Todos os campos são obrigatórios e não podem ficar em branco!')
            return redirect('basica')
        print(desnivel, vazao, potencia, mchs)
        lead = LeadBasica.objects.create(nome=nome,desnivel=desnivel, vazao=vazao,potencia=potencia,mchs=mchs)
        lead.save()

        dados = {
            'desnivel': desnivel,
            'vazao':vazao,
            'potencia':potencia,
            'mchs':mchs,
        }

        return render(request,'basica_resultado.html', dados)
    
    return render(request,'basica.html')
    

