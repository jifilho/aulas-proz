def calculadora(numeroUm, operacao, numeroDois):
    if operacao == "+":
        return numeroUm + numeroDois

    elif operacao == "-":
        return numeroUm - numeroDois

    elif operacao == "*":
      return numeroUm * numeroDois

    elif operacao == "/":
      return numeroUm / numeroDois

numeroUm = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numeroDois = float(input("Digite o segundo número: "))

resultado = calculadora(numeroUm, operacao, numeroDois)
print(resultado)
