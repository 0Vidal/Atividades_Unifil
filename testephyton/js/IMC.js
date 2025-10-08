function IMC(peso, altura){
    return peso / (altura*altura)
}

function calculaIMC(imc){
    if (imc < 19.5){
        return "Abaixo do peso"
    } else if(imc < 24.0){
       return "peso Normal"
    }else if(imc < 29.9){
        return "sobrepeso"
    }else if(imc < 34.9){
        return "Obesidade I"
    }else if(imc < 39.9){
        return "Obesidade II"
    }else{
        return "Obesidade III"
    }
}

let peso = 70;
let altura = 1.72;
let imc = IMC(peso,altura);
let classificacaoIMC = classificaIMC(imc);

console.log('IMC: ', imc)
console.log('Classificação do seu IMC: ', classificaoIMC)