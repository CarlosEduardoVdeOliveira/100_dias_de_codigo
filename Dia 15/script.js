const btnCounter = document.getElementById("btn-counter")
const counter = document.getElementById("counter");
const text = document.querySelector("textarea");

btnCounter.addEventListener('click', () =>{
  counter.textContent = text.value.length
});

text.addEventListener("input", ()=>{
  counter.textContent = text.value.length
})