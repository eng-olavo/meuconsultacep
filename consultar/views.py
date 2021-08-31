from django.shortcuts import render, redirect
import requests

def consultar(request):
    if request.GET:
        cep = request.GET.get('cep')
        print(cep)

        response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))

        dadoscep = response.json()

        print(dadoscep)

        return render(request, 'consultacep.html', dadoscep)