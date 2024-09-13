const circle = document.querySelector(".shape-color");
const input = document.querySelector("#input-shape-color");

function changeCircleColor(color) {
  circle.style.background = color;
}

input.addEventListener("input", () => {
  const color = input.value;
  changeCircleColor(color);
});

