
let role = document.getElementById("id_interestedRole");
let fn = document.getElementById("id_expertiseFunction");

document.onreadystatechange=function(){
//all onload actions
    fn.classList.add("ex-input");
    role.style.color = '#999';
    fn.style.color ='#999';
}

role.onchange = function colorChange() {
    var value = role.options[role.selectedIndex].value;
    console.log(value)
    if (value == "")
        role.style.color = '#999';
    else
        role.style.color = '#000';
}

fn.onchange = function colorChange() {
    var value = fn.options[fn.selectedIndex].value;
    console.log(value)
    if (value == "")
        fn.style.color = '#999';
    else
        fn.style.color = '#000';
}


let selectEx = document.querySelector('.selectEx');
//console.log(selectEx);

selectEx.onchange = function colorChange() {
  if (selectEx.value != 'null') {
    selectEx.style.color = '#000';
  } else {
    selectEx.style.color = '#999';
  }
}

