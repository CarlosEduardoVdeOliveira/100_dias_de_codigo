const circle = document.querySelector(".circle");
const inputColor = document.querySelector("#input-shape-color");
const textInfo = document.querySelector("#text-info")

function changeShapeCircleColor(color) {
  circle.style.background = color;
};
function changeSpanColor(color) {
  textInfo.style.background = color;
};

inputColor.addEventListener("input", () => {
  const color = inputColor.value;
  changeShapeCircleColor(color);
  changeSpanColor(color);
});

circle.addEventListener("click", () => {
  const color = getComputedStyle(circle).backgroundColor;
  return navigator.clipboard.writeText(color)
});

