let prompt = require('prompt-sync')();
const number1 = Number(prompt("Digite o primeiro numero: "));
const isEvenOrOdd = (number) => {

}
let sum = isEvenOrOdd(number1, number2);
if (isNaN(sum)) {
  throw new Error("Digite apenas números.\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente novamente.");
} else{
  console.log(`A soma de ${number1} + ${number2} = ${sum.toFixed(2)}`);
}

