
print("Sua massa corporal ")
peso = float(input("Qual é o seu peso em Quilogramas? "))
altura = float(input("Qual é a sua altura em Metros? "))
imc = peso / (altura**2)
print("Seu imc é ", round(imc/2,2))

if imc < 18.50:
    print("Abaixo do peso normal.")
elif imc <= 24.90:
    print("Peso normal.")
elif imc <= 29.90:
    print("Excesso de peso")
elif imc <= 34.90:
    print("Obesidade classe 1")
elif imc <= 39.90:
    print("Obesidade classe 2")
elif imc >= 40.00:
    print("Obesidade classe 3")







