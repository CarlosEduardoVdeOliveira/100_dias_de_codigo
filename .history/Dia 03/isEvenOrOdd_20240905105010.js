let prompt = require('prompt-sync')();
const number = Number(prompt("Digite um numero: "));
const isEvenOrOdd = (number) => {

}
let sum = isEvenOrOdd(number);
if (isNaN(sum)) {
  throw new Error("Digite apenas números.\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente novamente.");
} else{
  console.log(`O num ${number1} + ${number2} = ${sum.toFixed(2)}`);
}

