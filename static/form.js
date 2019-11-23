/*
  Main Street
  CS146 19F Final Project
  Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
*/

// login & register page
let alert = document.getElementById("flash");

// remove flashed alert after 3 seconds
if (alert != null){
  setTimeout(function(){
    alert.parentNode.removeChild(alert);
  }, 3000);
}

let socialAdder = document.getElementById("socialAdder"); // button to add social input
let hobbyAdder = document.getElementById("hobbyAdder");   // button to add hobby input

let addSocial = function(){
  // div that we're adding to
  let container = document.getElementById("social-container");


  let addDiv = function(parent){
    // create containing div to hold select and input
    let inputs = document.createElement("div");
    inputs.setAttribute("id", "social-platform");
    inputs.setAttribute("class", "socials");
    // create select childNode
    let select = document.createElement("select");
    select.setAttribute("name", "platform");
    select.setAttribute("class", "better-select");
    select.setAttribute("id", "platform");
    // create option childNodes
    let instagram = document.createElement("option");
    instagram.setAttribute("value", "Instagram");
    instagram.innerText = "Instagram";
    let snapchat = document.createElement("option");
    snapchat.setAttribute("value", "Snapchat");
    snapchat.innerText = "Snapchat";
    let twitter = document.createElement("option");
    twitter.setAttribute("value", "Twitter");
    twitter.innerText = "Twitter";
    // create input childNode
    let handle = document.createElement("input");
    handle.setAttribute("id", "socials");
    handle.setAttribute("type", "text");
    handle.setAttribute("name", "socials");
    handle.setAttribute("placeholder", "@bobbybob2");
    // create button childNode that removes this line of input
    let remove = document.createElement("button");
    remove.setAttribute("id", "removeButton");
    remove.setAttribute("type", "button");
    remove.setAttribute("class", "remover");
    remove.innerText = "❌"
    remove.addEventListener("click", function(){
      if (parent.childNodes.length > 2){
        parent.removeChild(inputs);
      }
    })
    select.appendChild(instagram);
    select.appendChild(snapchat);
    select.appendChild(twitter);
    inputs.appendChild(select);
    inputs.appendChild(handle);
    inputs.appendChild(remove);
    parent.appendChild(inputs);
  }
  if (container.childNodes.length < 4){
    addDiv(container);
  }

}


let addHobby = function(){
  // container for hobbies to be added
  let container = document.getElementById("hobby-container");
  let addInput = function(parent){
    let inputs = document.createElement("div");
    let hobby = document.createElement("input");
    hobby.setAttribute("id", "hobbies");
    hobby.setAttribute("name", "hobbies");
    hobby.setAttribute("placeholder", "Running, Frisbee, Sleep, Grading...");
    hobby.setAttribute("class", "hobby");
    hobby.required = true;
    // create button childNode that removes this line of input
    let remove = document.createElement("button");
    remove.setAttribute("id", "removeButton");
    remove.setAttribute("type", "button");
    remove.setAttribute("class", "remover");
    remove.innerText = "❌"
    remove.addEventListener("click", function(){
      if (parent.childNodes.length > 2){
        parent.removeChild(inputs);
      }
    })
    inputs.appendChild(hobby);
    inputs.appendChild(remove);
    parent.appendChild(inputs);

  }
  addInput(container);
}

addSocial() // initial social handle
socialAdder.addEventListener("click", addSocial);

addHobby() // initial hobby
hobbyAdder.addEventListener("click", addHobby);
