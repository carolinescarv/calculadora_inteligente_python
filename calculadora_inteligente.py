print("Bem-vindo à Calculadora Inteligente. Digite dois numeros e escolha a operação que deseja efetuar entre eles.")

continuar = "S"

while continuar == "S" or continuar == "s":
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  operacao = input("Digite a operação desejada (+, -, *, /)")

  if operacao == "+":
    print(f"{num1} + {num2} = {num1+num2}")
  elif operacao == "-":
    print(f"{num1} - {num2} = {num1-num2}")
  elif operacao == "*":
    print(f"{num1} * {num2} = {num1*num2}")
  elif operacao == "/":
    if num2 == 0:
      print("Erro: Divisão por zero não é permitida.")
    else:
      print(f"{num1} / {num2} = {num1/num2}")
  else:
    print("Operação inválida. Tente novamente.")

  continuar = input("Deseja realizar outra operação? Digite S para sim e N para não.")

else:
  print("Até a próxima!")
