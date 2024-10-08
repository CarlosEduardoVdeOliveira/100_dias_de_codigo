let prompt = require('prompt-sync')();
const number = Number(prompt("Digite um numero: "));

if (isNaN(number)) {
  throw new Error("Digite apenas números.\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente novamente.");
}
const isEvenOrOdd = (number) => number % 2 === 0 ? 'par' : 'ímpar';

let evenOrOdd = isEvenOrOdd(number);

console.log(`O número ${number} é ${evenOrOdd}`);

