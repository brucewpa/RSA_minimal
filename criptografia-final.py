# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:15:06 2016

@author: Bruce William Percílio Azevedo
"""

"""
    Objetivo: encontrar 2 primos que multiplicados formam o valor do universo que atua o RSA
    Parametros: valor do universo
    Retorno: vetor com 2 numeros primos
    tecnica: Força bruta
    Utilização: Pode ser ser customizada para ser utilizada em varias instancias, apenas inicializando o i com varios valores
"""
def primos(universo):
    primos = [] #Inicializa vetor
    #i = 9999695534909 #inicializa variavel com valor desejado
    i = 3#inicializa variavel com valor desejado
    while i*i <= universo: #se i*i maior que o valor do universo, a localização falhou
        while (universo % i) == 0: #se i dividido pelo universo tiver seu resto igual a 0, foi encontrado
            primos.append(i) # adiciona valor no vetor
            universo //= i # encontra o outro valor (que multilicado é igual ao universo)
        i += 2
    if (universo > 1):
        primos.append(universo) #adiciona o valor no vetor
    return primos

"""
    Objetivo: Realizar o calculo de fi
    Parametros: 2 numeros necessarios para o calculo de fi
    Retorno: valor resultante do calculo de fi
"""
def fi(x, y):
    return (x-1)*(y-1) #retorna o calculo de fi

"""
    Objetivo: decifrar mensagem cifrada por algorimo RSA
    Parametros: mensagam cifrava, chave privada, valor do universo RSA
    Retorno: mensagem em texto claro
"""
def decifrar(cifrado, priv_k, universo):
    return pow(cifrado, priv_k, universo)

"""
    Objetivo: Função recursiva para encontrar chave privada
    Parametros: chave publica, universo de fi
    Retorno: chave privada
"""
def extensao_chave_privada(aa, bb):
    ultimo, primeiro = abs(aa), abs(bb) # retorna os valores absolutos
    x, ultimox, y, ultimoy = 0, 1, 1, 0 # adicionar valores as variaveis
    while primeiro:
        ultimo, (quotient, primeiro) = primeiro, divmod(ultimo, primeiro)
        x, ultimox = ultimox - quotient*x, x #diminui o valorr de ultimox
        y, ultimoy = ultimoy - quotient*y, y #diminui o valor de ultimoy
    return ultimo, ultimox * (-1 if aa < 0 else 1), ultimoy * (-1 if bb < 0 else 1)
def chave_privada(pub_k, m):
    g, x, y = extensao_chave_privada(pub_k, m) #chama a função passando os argumentos
    if g != 1: #se o valor for diferente de 1
         raise ValueError
    return x % m



#p = 9999695534911
#q = 55180832909940433
universo = 551791528462201310857081956463
pub_k = 5178823383791929716166324671791
cifrado = 244137066175660768128879476899


compoemUniverso = primos(universo) #encontra os primos que compoem o universo
phi = fi(compoemUniverso[0],compoemUniverso[1]) #realiza conta de fi
priv_k =  chave_privada(pub_k, phi) #enontra a chave privada
claro = str(decifrar(cifrado, priv_k, universo)) #decifra o texto

i = 0
text = ""
while i < len(claro):
    text = text + ""+ chr((int(claro[i] +""+ claro[i+1])))
    i=i+2

print "p:"+str(compoemUniverso[0])
print "q:"+str(compoemUniverso[1])
print "Universo:"+str(universo)
print "Universo Fi:"+str(phi)
print "chave publica: "+str(pub_k)
print "chave privada: "+str(priv_k)
print "texto cifrado: "+str(cifrado)
print "texto ascii: "+claro
print "text claro:"+text[1:]
