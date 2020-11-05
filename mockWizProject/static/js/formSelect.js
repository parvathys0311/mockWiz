
let select = document.querySelector('.selectCdd');
console.log(select);

select.onchange = function colorChange() {
  console.log("1");
  if (select.value != 'null') {
    console.log('yes');
    select.style.color = '#000';
  } else {
    select.style.color = '#999';
  }
}

let selectEx = document.querySelector('.selectEx');
console.log(selectEx);

selectEx.onchange = function colorChange() {
  console.log("1");
  if (selectEx.value != 'null') {
    console.log('yes');
    selectEx.style.color = '#000';
  } else {
    selectEx.style.color = '#999';
  }
}

