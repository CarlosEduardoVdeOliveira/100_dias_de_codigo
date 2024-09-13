const prompt = require("prompt-sync")();
const number1 = Number(prompt("Digite o primeiro número: "));
const number2 = Number(prompt("Digite o segundo número: "));
const operator = Number(prompt("Digite a operação: "));
const addition = (installments1, installments2) => {
  return installments1 + installments2;
}
const subtraction = (minuend, subtrahend) => {
  return minuend - subtrahend;
}
const multiplication = (multiplier1, multiplier2) => {
  return multiplier1 * multiplier2;
}
const division = (dividend, divisor) => {
  if (divisor === 0) throw new Error("Não existe divisão por zero.");
  return dividend / divisor;
}
const calculator = (op, num1, num2) => {
  switch (op) {
    case "+":
        return addition(num1, num2);
      case "-":
        return subtraction(num1, num2);
      case "*":
        return multiplication(num1, num2);
      case "/":
        return division(num1, num2);
    default:
      return 'Operação inválida!'; 
    break;  
  }
}
if (isNaN(number1) || isNaN(number2)) {
  console.error("Erro: Operação ou números inválidos.\nNúmeros com casas decimais devem ser separados por ponto(.).\nOperações aceitas (+ - * /).\nTente novamente.");
}else{
  let result = calculator(operator, number1, number2);
  console.log(result);
  
}
