const aperturaMenuMovil = document.querySelector("#menu");
const menuMovil = document.querySelector("#menuMovil");
const cerrarMenu = document.querySelector("#cerrarMenu");

aperturaMenuMovil.addEventListener("click", () => {
  menuMovil.classList.add("active");
});

cerrarMenu.addEventListener("click", () => {
  menuMovil.classList.remove("active");
});
