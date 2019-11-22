/*
  Main Street
  CS146 19F Final Project
  Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
*/

// login & register page
alert = document.getElementById("flash")

// remove flashed alert after 3 seconds
if (alert != null){
  setTimeout(function(){
    alert.parentNode.removeChild(alert);
  }, 3000);
}
