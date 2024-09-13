let prompt = require('prompt-sync')();
const number1 = Number(prompt("Digite o primeiro numero: "))
const number2 = Number(prompt("Digite o segundo numero: "))
const sumNumbers = (number1, number2) => {
  let sum = 0;
  sum = number1 + number2;
  return sum;
}
let sum = sumNumbers(number1, number2);
if (isNaN(sum)) {
  throw new Error("Digite apenas números. Tente novamente.");
} else{
  console.log(`A soma de ${number1} + `);
}

