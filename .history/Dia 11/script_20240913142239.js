const circle = document.querySelector(".shape-color");
const inputColor = document.querySelector("#input-shape-color");
const textInfo = document.querySelector("#text")

function changeCircleColor(color) {
  circle.style.background = color;
};
function changeSpanColor(color) {
  circle.style.background = color;
};

inputColor.addEventListener("input", () => {
  const color = inputColor.value;
  changeCircleColor(color);
});

circle.addEventListener("click", () => {
  const color = getComputedStyle(circle).backgroundColor;
  return navigator.clipboard.writeText(color)
});

