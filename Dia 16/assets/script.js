let images = document.querySelectorAll("img");
let next = document.querySelector("#btn-next");
let previous = document.querySelector("#btn-previous");
let position = 0;

function transitionImage(image) {
  image.style.transition = "opacity 0.6s ease-in-out";
}

function hideAllImages() {
  images.forEach((img) => {
    img.style.opacity = 0;
  });
}

function showImage(index) {
  images[index].style.opacity = 1;
}

function nextImage() {
  hideAllImages();
  if (position === images.length - 1) {
    position = 0;
  } else {
    position++;
  }
  transitionImage(images[position]);
  showImage(position);
}

function previousImage() {
  hideAllImages();
  if (position === 0) {
    position = images.length - 1;
  } else {
    position--;
  }
  transitionImage(images[position]);
  showImage(position);
}

next.addEventListener("click", nextImage);
previous.addEventListener("click", previousImage);

setInterval(nextImage, 6000);

hideAllImages();
showImage(position);
