let prompt = require('prompt-sync')();
const number = Number(prompt("Digite um numero: "));
const isEvenOrOdd = (number) => {

}
let evenOrOdd = isEvenOrOdd(number);
if (isNaN(sum)) {
  throw new Error("Digite apenas números.\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente novamente.");
} else{
  console.log(`O número ${number} é: ${evenOrOdd}`);
}

