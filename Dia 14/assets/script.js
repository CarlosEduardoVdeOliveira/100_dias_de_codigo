const toggle = document.getElementById("toggle");
const links = document.querySelectorAll("a");
const form = document.querySelector("form");
const body = document.body;

function applyTheme (theme){
  if (theme === "dark") {
    links.forEach(link => link.classList.add("link-dark"));
    if(form) form.classList.add("form-dark");
    body.classList.add("body-dark");
    toggle.checked = true;
  }else{
    links.forEach(link => link.classList.remove("link-dark"));
    if(form) form.classList.remove("form-dark");
    body.classList.remove("body-dark");
    toggle.checked = false;
  }
}

toggle.addEventListener("click", () => {
  if (toggle.checked) {
    localStorage.setItem("theme", "dark");
    applyTheme("dark");
  } else {
    localStorage.setItem("theme", "light");
    applyTheme("light");
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme") || "light";
  applyTheme(savedTheme);
});