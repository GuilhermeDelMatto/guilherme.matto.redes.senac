def calculadora(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Operação inválida."

Numero1 = float(input("Digite o primeiro número: "))
Numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

resultado = calculadora(Numero1, Numero2, operacao)
print("Resultado:", resultado)