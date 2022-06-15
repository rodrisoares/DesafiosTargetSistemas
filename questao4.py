'''
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''
sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)

total = float(sp + rj + mg + es + out)

pSp = ((sp/total)*100)
pRj = ((rj/total)*100)
pMg = ((mg/total)*100)
pEs = ((es/total)*100)
pOut = ((out/total)*100)

print('O valor total mensal foi R$ {0:.2f} milhões'.format(total))

print('Porcentagem de SP  {0:.2f}%'.format(pSp))
print('Porcentagem de RJ  {0:.2f}%'.format(pRj))
print('Porcentagem de MG  {0:.2f}%'.format(pMg))
print('Porcentagem de ES  {0:.2f}%'.format(pEs))
print('Porcentagem de Outros {0:.2f}%'.format(pOut))

