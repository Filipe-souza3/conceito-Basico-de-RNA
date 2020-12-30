import random
import math

#entradas
entradas=[[1,1],[1,0],[0,1],[0,0]]
#pesos
pesos=[random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random(),random.random()]
#respostas corretas
resp=[0,1,1,0]
#bias
bias=[-1.0,-1.0,-1.0]
#taxa de aprendizado entre 0 e 1
n=0.5

def funcAtivacao(net):
    return 1/(1+math.exp(-net))

def funcBinario(e):
    if(e>=0.8):return 1
    else:return 0

    
for a in range(5000):
    for b in range(4):
        net1 = entradas[b][0]*pesos[0]+entradas[b][1]*pesos[1]+bias[0]*pesos[2]
        limiar1 = funcAtivacao(net1)
        
        net2 = entradas[b][0]*pesos[3]+entradas[b][1]*pesos[4]+bias[1]*pesos[5]
        limiar2 = funcAtivacao(net2)
        
        net3 = limiar1*pesos[6]+limiar2*pesos[7]+bias[2]*pesos[8]
        limiar3 = funcAtivacao(net3)


        #delta 
        delta5 = (resp[b]-limiar3)*limiar3*(1-limiar3)
        delta3 = (delta5*pesos[6])*limiar1*(1-limiar1)
        delta4 = (delta5*pesos[7])*limiar2*(1-limiar2)

        #pesoErro4 = delta5*limiar1
        #pesoErro5 = delta5*limiar2

        pesos[0]=pesos[0]+n*delta3*entradas[b][0]
        pesos[1]=pesos[1]+n*delta3*entradas[b][1]
        pesos[2]=pesos[2]+n*delta3*bias[0]

        pesos[3]=pesos[3]+n*delta4*entradas[b][0]
        pesos[4]=pesos[4]+n*delta4*entradas[b][1]
        pesos[5]=pesos[5]+n*delta4*bias[1]
        
        pesos[6]=pesos[6]+n*delta5*limiar1
        pesos[7]=pesos[7]+n*delta5*limiar2
        pesos[8]=pesos[8]+n*delta5*bias[2]       

        
        
print("==========================================================")
print("==========================================================")
print("==========================================================")
for b in range(4):
    net1 = entradas[b][0]*pesos[0]+entradas[b][1]*pesos[1]+bias[0]*pesos[2]
    limiar1 = funcAtivacao(net1)
    net2 = entradas[b][0]*pesos[3]+entradas[b][1]*pesos[4]+bias[1]*pesos[5]
    limiar2 = funcAtivacao(net2)
    net3 = limiar1*pesos[6]+limiar2*pesos[7]+bias[2]*pesos[8]
    limiar3 = funcAtivacao(net3)

    print("|",entradas[b][0]," ",entradas[b][1]," ",funcBinario(limiar3),"|", limiar3)
print(pesos[0],",",pesos[1],",",pesos[2],",",pesos[3],",",pesos[4],",",pesos[5],",",pesos[6],
      ",",pesos[7],",",pesos[8],"|||")

          