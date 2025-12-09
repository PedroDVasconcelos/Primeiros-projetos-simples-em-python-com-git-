def calculateTax(salario):
    if salario <= 1500:
        tax = 0.05

    elif salario <= 2500:
        tax = 0.15

    elif salario <= 3500:
        tax = 0.25
    
    else:
        tax = 0.30
    
    imposto = salario * tax
    return imposto

try:
    salario_Bruto = int(input("Digite seu salário:\n"))
    desconto = calculateTax(salario_Bruto)
    salario_Liquido = salario_Bruto - desconto
    
    if salario_Bruto < 0:
        print("Por favor, digite um valor de salário positivo.")
    else:
        valor_imposto = calculateTax(salario_Bruto)
        salario_liquido = salario_Bruto - valor_imposto

    print(f"Seu salário bruto é de {salario_Bruto}")

    print(f"Seu desconto é de {desconto}")

    print(f"Seu Salario liquido é de {salario_Liquido}")

except ValueError:
    print("Tente novamente")