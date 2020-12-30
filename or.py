import random
import math

#entradas
entradas=[[1,1],[1,0],[0,1],[0,0]]
#pesos
pesos=[random.random(),random.random()]
#respostas corretas
resp=[1,1,1,0]
#bias
bias=-1.0
#taxa de aprendizado entre 0 e 1
n=0.001

#limiar ativaçao do neuronio
def funcAtivacao(net):
    if(net>=0):return 1
    else:return 0

'''
for a in range(4):
    for treino in range(1000):
        net = entradas[a][0]*pesos[0]+entradas[a][1]*pesos[1]+bias
        limiar = funcAtivacao(net)
        #erro
        e = resp[a]-limiar

        print("|",entradas[a][0]," ",entradas[a][1]," ",limiar,"|")
        print("net: ",net)
        print("limiar: ",limiar)
        print("erro: ",e)
        print("peso 1: ",pesos[0])
        print("peso 2: ",pesos[1])
        print("bias: ",bias)
        print("====================")
        
        if(e==0):break
        #atualizar pesos
        pesos[0] = pesos[0]+n*e*entradas[a][0]
        pesos[1] = pesos[1]+n*e*entradas[a][1]
        bias=bias+n*e
'''

peso1=0.7501855863022028
peso2=0.8381110854771708
biass=-0.7489999999999998
for b in range(4):
    print("=======================")
    net = entradas[b][0]*peso2+entradas[b][1]*peso1+biass
    limiar=funcAtivacao(net)
    print("net: ",net)
    print("limiar ativaçao: ",limiar)    
    print("|",entradas[b][0]," ",entradas[b][1]," ",limiar,"|")
    
    print("=======================")
    
