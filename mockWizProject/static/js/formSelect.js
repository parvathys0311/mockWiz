let role = document.getElementById("id_interestedRole");
let fn = document.getElementById("id_expertiseFunction");
let yr = document.getElementById("yearsInterviewed");

document.onreadystatechange=function(){
//all onload actions
    fn.classList.add("ex-input");
    role.style.color = '#999';
    fn.style.color ='#999';
    yr.style.color = '#999';
}

role.onchange = function colorChange() {
    var value = role.options[role.selectedIndex].value;
    if (value == "")
        role.style.color = '#999';
    else
        role.style.color = '#000';
}

fn.onchange = function colorChange() {
    var value = fn.options[fn.selectedIndex].value;
    if (value == "")
        fn.style.color = '#999';
    else
        fn.style.color = '#000';
}

yr.onchange = function colorChange() {
    console.log("changed")
    var value_yr = yr.options[yr.selectedIndex].value;
    if (value_yr == "")
        yr.style.color = '#999';
    else
        yr.style.color = '#000';
}
