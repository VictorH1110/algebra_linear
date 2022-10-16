# função para dividir números com uma maior precisão
from re import X


def divFloat(x, y):
  a = b = 0

  if "." in str(x):
    a = len(str(x)) - str(x).find(".") -1
  if "." in str(y):
    b = len(str(y)) - str(y).find(".") -1
  num = max(a, b)

  factor = 10 ** num
  newx = x * factor
  newy = y * factor

  ans = (newx / newy)

  return (ans)


# função para ler uma matriz quadrada
def ler_matriz():
  matriz = []
  #lista_auxiliar = []
  
  print('Digite a matriz, linha por linha:\n[2 x ENTER para finalizar]')
  while(True):
    lista_auxiliar = [int(i) for i in input().split()]
    if len(lista_auxiliar) == 0:
      break
    matriz.append(lista_auxiliar[:])
    lista_auxiliar.clear()

  return matriz

# função para calcular a determinante de uma matriz quadrada
def determinante(matriz:list):
  dimensao = len(matriz)
  troca = 1
  determinante = 1

  for pivot in range(dimensao-1):
    for linha in range(pivot+1, dimensao):
      # verifica se há 0 na diagonal principal, caso haja troca as linhas
      if matriz[pivot][pivot] == 0:
        for zero in range(pivot+1, dimensao):
          if matriz[zero][pivot] != 0:
            lista_troca = matriz[pivot]
            matriz[pivot] = matriz[zero]
            matriz[zero] = lista_troca
            troca = -troca
            # adicionado o break para sair do for apos uma troca de linha
            break
      # checa se há divisão por 0 e faz a razão
      try:
        # utilizando a função divFloat
        razao = -(divFloat(matriz[linha][pivot], matriz[pivot][pivot]))
      except:
        return 0
      # troca os valores a fim de montar a matriz triangular
      for i in range(dimensao):
        matriz[linha][i] = matriz[linha][i]+(matriz[pivot][i] * razao)
      
  # calcula a determinante
  for i in range(dimensao):
    determinante *= matriz[i][i]
  
  return determinante * troca

def inversa(matriz:list):
  dimensao = len(matriz)
  matriz_identidade = []
  lista_auxiliar = []

  for i in range(dimensao):
    for j in range(dimensao):
      if i == j:
        lista_auxiliar.append(1)
      else:
        lista_auxiliar.append(0)
    matriz_identidade.append(lista_auxiliar[:])
    lista_auxiliar.clear()

  for pivot in range(dimensao):
    dividido = matriz[pivot][pivot]
    for linha in range(dimensao):
      if linha == pivot:
        continue
      # verifica se há 0 na diagonal principal, caso haja troca as linhas
      if matriz[pivot][pivot] == 0:
        for zero in range(pivot+1, dimensao):
          if matriz[zero][pivot] != 0:
            lista_troca = matriz[pivot]
            lista_troca2 = matriz_identidade[pivot]
            matriz[pivot] = matriz[zero]
            matriz_identidade[pivot] = matriz_identidade[zero]
            matriz[zero] = lista_troca
            matriz_identidade[zero] = lista_troca2
            dividido = matriz[pivot][pivot]
            # adicionado o break para sair do for apos uma troca de linha
            break
      # checa se há divisão por 0 e faz a razão
      # utilizando a função divFloat
      razao = -matriz[linha][pivot]
      # troca os valores a fim de montar a matriz triangular
      for i in range(dimensao):
        try:
          if (pivot == 0 and linha == 1) or linha == 0:
            matriz[pivot][i] = divFloat(matriz[pivot][i], dividido)
            matriz_identidade[pivot][i] = divFloat(matriz_identidade[pivot][i], dividido)
          matriz[linha][i] = matriz[linha][i]+(matriz[pivot][i] * razao)
          matriz_identidade[linha][i] = matriz_identidade[linha][i]+(matriz_identidade[pivot][i] * razao)
        except:
          return print('Matriz não admite inversa.')
    
  return matriz_identidade

# função para multiplicar duas matrizes
def multMatrix(matriz1:list, matriz2:list):
  matriz = []
  lista_auxiliar = []
  tamanho = len(matriz1)

  for i in range(tamanho):
    for j in range(tamanho):
      soma = 0
      for k in range(tamanho):
        soma += matriz1[i][k] * matriz2[k][j]
      lista_auxiliar.append(soma)
    matriz.append(lista_auxiliar[:])
    lista_auxiliar.clear()

  return matriz

# função que lê um número n de bases e as transforma em colunas de uma matriz
def baseToMatrix(base):

  new_matriz = []
  lista_auxiliar = []
  for i in range(len(base[0])):
    for j in range(len(base[0])):
      lista_auxiliar.append(base[j][i])
    new_matriz.append(lista_auxiliar[:])
    lista_auxiliar.clear()

  return new_matriz

# função para matriz de mudança de base
def matrixBaseChanger(bmatriz1:list, bmatriz2:list):
  dic = {}
  if determinante(bmatriz1) == 0:
    dic["base1"] = "Erro! Base 1 não é L.I"
  if determinante(bmatriz2) == 0:
    dic["base2"] = "Erro! Base 2 não é L.I"
  if not dic:
    return multMatrix(inversa(bmatriz1), bmatriz2)
  else:
    return dic




