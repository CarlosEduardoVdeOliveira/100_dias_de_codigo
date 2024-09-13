let prompt = require('prompt-sync')();
const number = Number(prompt("Digite um numero: "));
const isEvenOrOdd = (number) => {
  const evenOrOdd = number % 2 === 0 ? 'par' : 'impar';
  return evenOrOdd;
}
let evenOrOdd = isEvenOrOdd(number);
if (isNaN(number)) {
  throw new Error("Digite apenas números.\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente novamente.");
}
  console.log(`O número ${number} é: ${evenOrOdd}`);
}

