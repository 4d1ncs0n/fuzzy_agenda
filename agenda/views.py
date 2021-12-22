from django.shortcuts import render
import requests
import subprocess
import sys


def button(request):
    '''
    respuesta del botón
    '''
    return render(request, 'home.html')

def output(request):
    '''
    lineas para extracción
    '''
    input_ = request.POST.get('param')
    ejecutable = [sys.executable, 'request.py', input_]
    process = subprocess.run(
        args=ejecutable,
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding='utf-8'
    )
    return render(request, 'home.html', {'data': process.stdout})
