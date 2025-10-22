def calcula_IMC(peso,altura):
    return peso / (altura * altura)

def classificar_IMC(imc):
    if imc < 19.5:
        return "Abaixo do peso"
    elif imc < 24.0:
       return "peso Normal"
    elif imc < 29.9:
        return "sobrepeso"
    elif imc < 34.9:
        return "Obesidade I"
    elif imc < 39.9:
        return "Obesidade II"
    else:
        return "Obesidade III"
    
peso = 72;
altura = 1.72;
imc = calcula_IMC(peso, altura);
classificacao_IMC = classificar_IMC(imc);

print("IMC: ", imc)
print("Classificação do IMC: ", classificacao_IMC)