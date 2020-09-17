import re

finename = "sequencias.fasta"

match = int (1)
mismatch = int(-1)
gaps = int (-2) 

#lendo o arquivo .fasta
with open(finename) as f:
    arquivo = f.readlines()

#transformando o arquivo em string
sequencia = ''.join(arquivo)

#dividindo cada fita
fitaCodificadora = re.split('\n', sequencia)

s = re.split('', fitaCodificadora[0])
f = re.split('', fitaCodificadora[1])

s.pop()#deleta ultimo
s.pop(0)#deleta primeiro
f.pop()#deleta ultimo
f.pop(0)#deleta primeiro
s.insert(0, '-')
f.insert(0, '-')

tam_coluna = len(f)
tam_linha = len(s)

lista_i = []
lista_j = []
score = 0


#função para exibir a matriz 
def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

#criando uma matriz vazia
matriz = []

for i in range(tam_linha): #linha
    linha = []
    for j in range(tam_coluna): #coluna 
        elemento = ''
        linha.append(elemento)
    matriz.append(linha)

#iniciando a matriz 
for i in range(tam_linha): #linha 
    if s[i] == '-' and f[0] == '-':
        score = score + 0
        matriz[i][0] = score #altera o elemento
    elif s[i] == '-' and f[0] != '-' or s[i] != '-' and f[0]  == '-':
        score = score + gaps
        matriz[i][0] = score
    elif  s[i] != f[0]:
        score = score + mismatch
        matriz[i][0] = score
    else:#se for igual 
        socre = score + match
        matriz[i][0] = score

score = 0

for j in range(tam_coluna): #coluna
    if s[0] == '-' and f[j] == '-':
        score = score + 0
        matriz[0][j] = score 
    elif s[0] == '-' and f[j] != '-' or s[0] != '-' and f[j]  == '-':
        score = score + gaps
        matriz[0][j] = score
    elif  s[0] != f[j]:
        score = score + mismatch
        matriz[0][j] = score
    else:#se for igual 
        socre = score + match
        matriz[0][j] = score 

score = 0
v = 0 #vertical
h = 0 #horizontal
d = 0 #diagonal

for i in range(tam_linha): #linha
    for j in range(tam_coluna): #coluna
        if(matriz[i][j] == ''): #for vazia
            #vertical
            v = matriz[i-1][j] + (gaps)
            #horizontal
            h = (matriz[i][j-1] + (gaps))
            #diagonal
            if(s[i] == f[j]):#listas de sequencias
                d = matriz[i-1][j-1] + (match)
            else:
                d = matriz[i-1][j-1] + (mismatch)
            #verifcando qual é o maior
            maior = [v, h, d]
            score_maior  = max(maior)
            matriz[i][j] = score_maior
            
exibir_matriz(matriz)

#Alinhamento global
alinhamento_s = []

elem = matriz[tam_linha-1][tam_coluna-1]

i = tam_linha-1
j = tam_coluna-1
aux_s = []
alinhamento_f = []

while(i > 0 and j > 0):
    
    elem  = matriz[i][j]

    if ((matriz[i-1][j]) + (gaps)) == elem:#vertical         
        alinhamento_s.append(s[i])
        alinhamento_f.append('-')
        i = i-1
  
    elif ((matriz[i][j-1]) + (gaps)) == elem:#horizontal
        alinhamento_s.append('-')
        alinhamento_f .append(f[j])
        j = j-1 
        
    elif (((matriz[i-1][j-1]) + (match)) == elem) or (((matriz[i-1][j-1]) + (mismatch)) == elem) :#diagonal    
        alinhamento_s.append(s[i])
        alinhamento_f .append(f[j])
        i = i-1
        j = j-1 
 
print('\n')
print(alinhamento_f[::-1])
print(alinhamento_s[::-1])
