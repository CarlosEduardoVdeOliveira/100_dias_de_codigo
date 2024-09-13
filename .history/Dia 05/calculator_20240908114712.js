const pormpt = require('prompt-sync')();
const expression = prompt("Digite a expressão para fazer o calculo: ");

const calculator = (expression) => {
  try {
    let result = eval(expression);
    return result;
  } catch (error) {
    throw new Error("");
  }
}