'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

dados = open("dados.json")
data = json.load(dados)

def menor_valor():
    dia = 0
    menorValor = 0
    contador = 0
    for i in data:
        if i["valor"] > 0:
            if contador < 1:
                menorValor = (i["valor"])
                contador = contador + 1
            else:
                valorInicial = (i["valor"])
                if valorInicial <= menorValor:
                    menorValor = valorInicial
                    dia = i['dia']
                        
    print("O menor faturamento foi no Dia",dia, "R$", menorValor, ".")

def maior_valor():
    dia = 0
    maiorValor = 0
    for i in data:
        if i["valor"] > 0:
            valorInicial = (i["valor"])
            if valorInicial >= maiorValor:
                maiorValor = valorInicial
                dia = i['dia']
                
    print("O maior faturamento foi no Dia",dia, "R$", maiorValor, ".")

def media_mensal():
    dias = 0
    soma = 0
    divisor = 0
    for i in data:
        if i["valor"] > 0:
            soma = soma +(i["valor"])
            divisor = divisor + 1
    media = soma/divisor
    print("A media mensal é de R$", round(media, 4))
    for i in data:
            if i["valor"] > media:
                dias = dias + 1
    print("Em", dias, "dias o faturamento foi superior a média")

menor_valor()
maior_valor()
media_mensal()