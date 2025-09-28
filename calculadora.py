import math

def calculadora():

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break

        except:
            print("error valor digitado não é valido.")
        

    print("\n ‼️ AVISO: Caso escolha raiz quadrada(sqrt) o segundo numero é ignorado. ‼️ \n")
    operacao = input("escolha a operação: + , -, *, /, **, sqrt(para raiz quadrada).")


    if operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "*":
        print(num1 * num2)
    elif operacao == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("indefinido")
    elif operacao == "**":
        print(num1 ** num2)
    elif operacao == "sqrt":
        if num1 >=0:
            print(math.sqrt(num1))
        else:
            print("error: raiz quadrada de número negativo não é real.")    
    else:
        print("Operação invalida escolha entre +, -, *, /, **, sqrt.")

if __name__ == "__main__":
    calculadora()