const inputSizePassword = document.querySelector("#input-size-password");
const btnGeneratePassword = document.querySelector("#btn-generate-password");
const divInput = document.querySelector(".group-input");
const divContentPassword = document.querySelector(".content-password");

const divResultPassword = document.querySelector(".result-password");
const btnGenerateNewPassword = document.querySelector("#btn-generate-new-password");
const copy = document.querySelector("#btn-copy");

function getRandomArbitrary() {
  return Math.round(Math.random() * (126 - 33) + 33);
}

function createPassword(size){
  let password = "";
  while(password.length < size){
    password += String.fromCharCode(getRandomArbitrary());
  }
  return password;
}

function generateContent(password){
  const p = document.createElement("p");
  p.textContent = password;
  p.value = password;
  p.classList.add("result")
  divInput.style.display = "none";
  inputSizePassword.value = "";
  divContentPassword.style.display = "flex";
  divResultPassword.appendChild(p);
}

function generateNewPassword (){
  divInput.style.display = "flex";
  divContentPassword.style.display = "none";
  divResultPassword.textContent = "";
}

function generatePassword(){
  let getSizePassword = Number(inputSizePassword.value);
  let password = createPassword(getSizePassword);
  if (getSizePassword <= 3) return alert("A senha deve ter no mínimo 3 carácter");
  createPassword(getSizePassword);
  generateContent(password);
}

function copyPassword(){
  let result = document.querySelector(".result").textContent;
  navigator.clipboard.writeText(result).then(() => {
    alert("Senha copiada para área de transferência.");
  }).catch(err => {
    console.error("Erro ao copiar a senha: ", err);
  });
}

copy.addEventListener("click", copyPassword);
btnGenerateNewPassword.addEventListener("click", generateNewPassword);
btnGeneratePassword.addEventListener("click", generatePassword);
