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
  print("Hello from a function")

def calcularNumOnda():
  print("hello 2")

def calculaFreqAngular():
  print("hello 3")

def calculaCompriOnda():
  print("hello 4")

main()