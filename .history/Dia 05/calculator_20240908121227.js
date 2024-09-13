const prompt = require('prompt-sync')();

const calculator = (expression) => {
  try {
    let result = eval(expression);
    return result;
  } catch (error) {
    throw new Error("Erro: verifique se a expressão contém apenas: números e operadores (+, -, *, /)\nNúmeros com casas decimais devem ser separados por ponto(.).\nTente nova");
  }
}
const expression = prompt("Digite a expressão matemática que deseja calcular (ex: 2 + 3 * 4 / 2): ");
try {
  let result = calculator(expression);
  console.log(`O resultado de ${expression} = ${Number(result)}`);
} catch (error) {
  console.error(error.message);
  
}
