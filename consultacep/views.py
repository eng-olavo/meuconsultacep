from django.shortcuts import render, redirect
import requests

# Create your views here.



def consultacep(request):

    return render(request,'consultacep/consultacep.html')

