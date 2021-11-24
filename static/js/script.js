let el = document.getElementById("wrapper");
let toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
  el.classList.toggle("toggled");
};

for (let i = 0; i < document.getElementsByClassName("money").length; i++) {
  let money_elm = document.getElementsByClassName("money")[i];
  let money_elm_value = money_elm.innerHTML;
  money_elm.innerHTML = money_elm_value.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
