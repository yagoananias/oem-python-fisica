def main():

  running = True
  while running == True:
    print("---- Menu ----")
    print("1 - Entrar com o comprimento de onda: ")
    print("2 - Entrar com a frequência da onda em [Hz]: ")
    print("3 - Sair")
    print("--------------")

    #variavel para guardar a escolha do menu
    opcao = input("Escolha a opcao desejada: ")

    if opcao == "1":
      calculaFrequencia()
      calcularNumOnda()
      calculaFreqAngular()
    elif opcao == "2":
      calculaCompriOnda()
      calcularNumOnda()
      calculaFreqAngular()
    elif opcao == "3":
      running = False

def calculaFrequencia():
  global c
  c = 3*10^8

  comprimentoLambda = float(input("Digite o comprimento de onda: "))
  unidade = input("Digite a unidade nm, um, mm, m ou km: ")
  
  if unidade == "nm":
    frequencia = c / comprimentoLambda
    print("A frequência é: %.3f Hz." %frequencia)
  elif unidade == "um":
    print("calcula um")
  elif unidade == "mm":
    print("calcula mm")
  elif unidade == "m":
    print("calcula m")
  elif unidade == "km":
    print("calcula km")


def calcularNumOnda():
  print("hello 2")

def calculaFreqAngular():
  print("hello 3")

def calculaCompriOnda():
  print("hello 4")

main()
