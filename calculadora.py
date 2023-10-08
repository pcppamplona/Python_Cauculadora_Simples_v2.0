
def potencia(a: int, b: int):
  return a ** b


def divisao(a: int, b: int):
  return a / b


def multiplicacao(a: int, b: int):
  return a * b


def subtracao(a: int, b: int):
  return a - b


def soma(a: int, b: int):
  return a + b


a = int(input("Digite o primeiro valor: "))
operacao = input("+: Soma\n-: Subtração\n*: Multiplicação\n/: Divisão\n**: Exponenciação..:")
b = int(input("Digite o segundo valor: "))

if operacao == '+':
  resultado = soma(a, b)

elif operacao == '-':
  resultado = subtracao(a, b)

elif operacao == '*':
  resultado = multiplicacao(a, b)

elif operacao == '/':
  resultado = divisao(a, b)

elif operacao == '**':
  resultado = potencia(a, b)

else:
  print('operador nao reconhecido')

print (resultado)
