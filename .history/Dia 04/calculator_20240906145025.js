//Desafio: Crie uma calculadora simples que realiza operações de adição, subtração, divisão e multiplicação.
const addition = (installments1, installments2) => {
  return installments1 + installments2;
}
const subtraction = (minuend, subtrahend) => {
  return minuend - subtrahend;
}
const division = (dividend, divisor) => {
  if (divisor === 0) throw new Error("Não existe divisão por zero.");
  return dividend / divisor;
}
const multiplication = (multiplier1, multiplier2) => {
  return multiplier1 * multiplier2
}