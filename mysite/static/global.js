const dropwon = document.getElementById("menu");
const menu = document.getElementById("Categorias-menu");
dropwon.addEventListener("mousemove", () => {
  let actualStyle = menu.style.display;
  console.log(actualStyle);
  menu.style.display = actualStyle === "none" ? "block" : "none";
});
