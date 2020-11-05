// Navbar Toggle Menu

// Declare our element variables
const navBarToggle = document.querySelector('.toggle');
const menu = document.querySelector('header');
console.log(menu)

// function statement
function menuToggle() {
  console.log('Menu is toggled');
  if (menu.classList.contains('active')){
    // console.log("if")
    menu.classList.remove('active')
  } else {
    // console.log('else') 
    menu.classList.add('active');
  }
}

// The code in the `eventHandler` function (defined above) will be invoked each time `button` is clicked
navBarToggle.addEventListener('click', menuToggle, false);