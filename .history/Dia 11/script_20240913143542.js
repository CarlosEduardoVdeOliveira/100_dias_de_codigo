const circle = document.querySelector(".circle");
const inputColor = document.querySelector("#input-select-color");
const textInfo = document.querySelector(".text-select-color")

function changeShapeCircleColor(color) {
  circle.style.background = color;
};
function changeSpanColor(color) {
  textInfo.style.color = color;
};

inputColor.addEventListener("input", () => {
  const color = inputColor.value;
  changeShapeCircleColor(color);
  changeSpanColor(color);
});

circle.addEventListener("click", () => {
  const color = getComputedStyle(circle).backgroundColor;
  navigator.clipboard.writeText(color)
  alert("Cor copiada para area de transferência.")
});

