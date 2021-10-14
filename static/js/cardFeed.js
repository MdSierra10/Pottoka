const comentarios = document.querySelector("#comentarios");
const comentar = document.querySelector("#comentar");
comentar.addEventListener("click", () => {
  comentarios.classList.toggle("active");
});
