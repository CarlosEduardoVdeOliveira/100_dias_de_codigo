let prompt = require('prompt-sync')();
const number1 = Number(prompt("Digite o primeiro numero: "))
const number2 = Number(prompt("Digite o segundo numero: "))
const sumNumbers = (number1, number2) =>{ 
  number1 + number2;
}

console.log(sumNumbers(number1, number2));
