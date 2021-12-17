for (let i = 0; i < document.getElementsByClassName("money").length; i++) {
  let money_elm = document.getElementsByClassName("money")[i];
  let money_elm_value = money_elm.innerHTML;
  money_elm.innerHTML = `&#8377;${format_ammount(parseInt(money_elm_value))}`;
}

function format_ammount(number) {
  return Intl.NumberFormat("en-IN").format(number);
}
