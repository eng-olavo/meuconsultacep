from django.shortcuts import render, redirect
import requests

def consultar(request):
    if request.GET:
        cep = request.GET.get('cep')
        print(cep)

        response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))

        dadoscep = response.json()

        print(dadoscep)

        print('logr : ' + dadoscep['logradouro'])
        print('comp : ' + dadoscep['complemento'])
        print('bair : ' + dadoscep['bairro'])
        print('loca : ' + dadoscep['localidade'])
        print('__uf : ' + dadoscep['uf'])
        print('_cep : ' + dadoscep['cep'])

    return 'ok'

#redirect('/consultacep.html')

