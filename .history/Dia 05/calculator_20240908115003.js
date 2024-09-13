const prompt = require('prompt-sync')();
const expression = prompt("Digite a expressão para fazer o calculo: ");

const calculator = (expression) => {
  try {
    let result = eval(expression);
    return result;
  } catch (error) {
    throw new Error("Erro: verifique se a expressão contém apenas: números e operadores (+, -, *, /)");
  }
}
let result = calculator(expression);
console.log(`O resultado de ${expression} = ${result.toFixed(2)}`);
