from django.shortcuts import render, redirect
import math
from django.contrib import messages
from .models import LeadAvancada

def avancada(request):
    #DATA INPUT FROM USER
    if request.method == 'POST':
        nome = request.POST['nome']
        desnivel = int(float(request.POST['desnivel']))
        vazao = int(float(request.POST['vazao']))
        dist_hidr = int(float(request.POST['dist_hidr']))
        dist_eletrica = int(float(request.POST['dist_eletrica']))
        modelo = request.POST['modelo']
        tipo_cabo = request.POST['tipo_cabo']
        print(nome,desnivel,vazao,modelo,tipo_cabo)

        #CALCULATIONS
        diametro_econ = 0
    
        potencia = desnivel*vazao*9.81*0.531
        
        diametro_econ = 123.7*(((float(vazao)/1000)**3)/(1.2*float(desnivel)))**(1/7)*10
        
        tubos_comerciais = [75,100,125,150,200,250,300,350,400,450,500,550,600,650,700,750,800]
        tubos_comerciais.sort()
        
        diametro_comercial = math.ceil(diametro_econ)
        
        for i in tubos_comerciais:
            if diametro_comercial < i:
                diametro_comercial = i
                break
                
        vel_escoamento = (4*float(vazao)/1000)/((math.pi)*((diametro_comercial/1000)**2))
        
        perda_carga_unit = (vel_escoamento/(0.355*140*(diametro_comercial/1000)**0.63))**(1/0.54)
        
        perda_carga_tub = perda_carga_unit*dist_hidr

        print(potencia,diametro_econ,diametro_comercial,vel_escoamento,perda_carga_unit,perda_carga_tub)

        k = 3.6

        perda_carga_conex_total = k*(vel_escoamento**2)/(2*9.81)
    
        if perda_carga_tub + perda_carga_conex_total <= desnivel:
            perda_carga_total = perda_carga_tub + perda_carga_conex_total
            
        else:
            messages.error(request, 'A perda de carga não pode ser maior do que o desnível do terreno.')
            return redirect('avancada')

        desnivel_real = desnivel - perda_carga_total
    
        porcentagem_perda = (perda_carga_total / desnivel)
        
        potencia = vazao*desnivel_real*9.81*0.64

        mchs = potencia/1000
        if potencia%1000 >= 500:
            mchs = math.ceil(mchs)
        else:
            mchs = math.floor(mchs)

        print(modelo)

        if modelo == 220:
            modelo = 'Off Grid'
        else:
            modelo = 'On Grid'

        if tipo_cabo == 0.0282:
            tipo_cabo = 'Cobre'
        else:
            tipo_cabo = 'Alumínio'

        lead = LeadAvancada.objects.create(nome=nome,desnivel=desnivel, vazao=vazao,potencia=potencia,mchs=mchs,dist_hidr=dist_hidr,dist_eletr=dist_eletrica, modelo=modelo)
        lead.save()

        dados = {
            'desnivel':desnivel,
            'vazao':vazao,
            'dist_hidr':dist_hidr,
            'dist_eletrica':dist_eletrica,
            'modelo':modelo,
            'tipo_cabo':tipo_cabo,
            'diametro_econ':diametro_econ,
            'diametro_comercial':diametro_comercial,
            'vel_escoamento':vel_escoamento,
            'perda_carga_unit':perda_carga_unit,
            'perda_carga_tub':perda_carga_tub,
            'perda_carga_conex_total':perda_carga_conex_total,
            'desnivel_real':desnivel_real,
            'porcentagem_perda':"{0:.0%}".format(porcentagem_perda),
            'potencia':potencia,
            'mchs':mchs,         
        }

        return render(request,'avancada_resultado.html', dados)
    
    return render(request,'avancada.html')

