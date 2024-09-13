let prompt = require('prompt-sync')();
const number1 = Number(prompt("Digite o primeiro numero: "))
const number2 = Number(prompt("Digite o segundo numero: "))
const sumNumbers = (number1, number2) => {
  let sum = 0;
  if (isNaN(number1) && isNaN(number2)) return throw new Error("");
  sum = number1 + number2;
  return sum;
}

console.log(sumNumbers(number1, number2));
