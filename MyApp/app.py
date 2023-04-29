import re

from classes import CalculateIPV4
from flask import Flask, render_template, request

app = Flask(__name__)


texto_cabecalho = 'Redes IPV4' 
caminho_texto = './arquivos_texto/'

@app.route('/')
def index ():
    nome_pagina = 'Redes IPV4'      
      
    subtitulo = ['Divisão em Sub-redes', 'Necessidade de uma calculadora IPv4 de sub-rede',
                 'Calculo Redes IPV4']         
    texto1 = ''
    texto2 = ''
    texto_input = 'Digite o IP da rede + Bit: '

    with open(f'{caminho_texto}divisao.txt','r', encoding='utf-8') as file:
        texto1 += file.read()

    with open(f'{caminho_texto}necessidade.txt','r', encoding='utf-8') as file:
        texto2 += file.read()

    return render_template('index.html', nome_pagina=nome_pagina,   
                           texto_cabecalho = texto_cabecalho,                        
                           subtitulo1 = subtitulo[0],
                           subtitulo2 = subtitulo[1],
                           subtitulo3 = subtitulo[2],
                           texto1 = texto1,
                           texto2 = texto2,
                           texto_input = texto_input)


@app.route('/validar', methods=['POST',])
def validar():    
    nome_pagina = 'Redes IPV4'
    ip_form = request.form['IP']
    texto_resultado = ['IP','Prefixo', 'Mascara de Sub-Rede', 
                       'IP de Rede','IP de Broadcast', 'Hosts']
    subtitulos = ['IP', 'Mascara Sub-Rede', 'Hosts']

    texto_input = 'Digite o IP da rede + Bit: '

    arquivos = arquivos_texto()                       

    ip_regexp = re.compile(
            r'^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/[0-3]{1}([0-9]{1})?$')

    if ip_regexp.search(ip_form):
        valor = True
        retorno = CalculateIPV4(ip=ip_form)
        resultado = [retorno.separete_ip()[0], retorno.separete_ip()[1], 
                     retorno.network_mask(), retorno.network_ip(), 
                     retorno.Broadcast_ip(), retorno.total_hosts()]         
    else:
        resultado = 'Digite um IP válido'  
        valor = False


    return render_template('resultado.html', resultado=resultado, 
                           valor=valor,
                           texto_cabecalho = texto_cabecalho,
                           nome_pagina = nome_pagina,
                           ip = texto_resultado[0],
                           prefixo = texto_resultado[1],
                           mascara = texto_resultado[2],
                           ip_rede = texto_resultado[3],
                           ip_broadcast = texto_resultado[4],
                           hosts = texto_resultado[5],
                           texto_ip = arquivos[0],
                           texto_hosts = arquivos[1],
                           texto_mascara = arquivos[2],
                           subtitulo1 = subtitulos[0],
                           subtitulo2 = subtitulos[1],
                           subtitulo3 = subtitulos[2],
                           texto_input = texto_input                           
                           )

def arquivos_texto():
    ip = ''
    hosts = ''
    mascara_rede = ''

    with open(f'{caminho_texto}ip.txt', 'r', encoding='utf-8') as file:
        ip += file.read()

    with open(f'{caminho_texto}hosts.txt', 'r', encoding='utf-8') as file:
        hosts += file.read()

    with open(f'{caminho_texto}mascara.txt', 'r', encoding='utf-8') as file:
        mascara_rede += file.read()

    return ip, hosts, mascara_rede

if __name__=='__main__':
    app.run(debug=True)
