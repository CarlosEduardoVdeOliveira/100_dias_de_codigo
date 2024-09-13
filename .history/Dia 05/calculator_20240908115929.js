const prompt = require('prompt-sync')();
const expression = prompt("Digite a expressão para fazer o calculo: ");

const calculator = (expression) => {
  try {
    let result = eval(expression);
    return result;
  } catch (error) {
    throw new Error("Digite a expressão matemática que deseja calcular (ex: 2 + 3 * 4 / 2): ");
  }
}
let result = calculator(expression);
console.log(`O resultado de ${expression} = ${result.toFixed(2)}`);
