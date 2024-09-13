const circle = document.querySelector(".shape-color");
const inputColor = document.querySelector("#input-shape-color");

function changeCircleColor(color) {
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

