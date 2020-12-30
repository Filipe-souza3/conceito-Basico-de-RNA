import random
import math


#entradas
entradas = [[1,1], [1,0], [0,1], [0,0]]
#pesos
pesos  = [random.random(), random.random()]
#repostas certas
resp = [1,0,0,0]
#bias
bias = -1.0#random.random()
#taxa de aprendizado entre 0e 1
n=0.001

#derivada - taxa de variação entre 2 pontos
def derivada(n):
    return n*(1-n)


#limiar de disparo do neuronio
def funcAtivacao(net):
    if(net>=0):return 1
    else:return 0

#epocas  -  treinamento do perceptron
print("peso 1: ",pesos[0])
print("peso 2: ",pesos[1])
print("bias: ",bias)
for b in range(4):
   
    for a in range (1000):
        
        net = entradas[b][0]*pesos[0]+entradas[b][1]*pesos[1]+bias
        print("NET: ",net)
        limiar = funcAtivacao(net)
        print("limiar ativação: ",limiar)    
        #erro = resposta esperada - respota gerada
        e = resp[b]-limiar
        print("|",entradas[b][0]," ",entradas[b][1]," ",limiar,"|")
        if(e==0):
            print('achou valor esperado')
            break
        print("erro: ",e)
        #atualizar pesos
        pesos[0] = pesos[0]+n*e*entradas[b][0]
        pesos[1] = pesos[1]+n*e*entradas[b][1]
        bias = bias+n*e
        print("peso 1: ",pesos[0])
        print("peso 2: ",pesos[1])
        print("bias: ",bias)
        
        print("=======")


#teste com os pesos achados acima
'''print("=================================")
pesos1=0.4809813621280734#0.18222621820123397
pesos2=0.4000737607592577#0.2718078652049982
biass =-0.8789999999999999#-0.35818465296740687

for ent in range(4):
    net = entradas[ent][0]*pesos1+entradas[ent][1]*pesos2+biass
    print("NET: ",net)
    limiar = funcAtivacao(net)
    print("limiar ativação: ",limiar) 
    print("|",entradas[ent][0]," ",entradas[ent][1]," ",limiar,"|")
    print("=================================")'''
      

