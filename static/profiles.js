/*
  Main Street
  CS146 19F Final Project
  Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
*/

let username = document.getElementById("user").innerText;

// AJAX retrieves socials
let retrieveSocials = function(){
  let contacts = document.getElementById("profile-contacts")
  let socials = "";
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            socials = this.responseText.split(",");
            socials = socials.filter(function(handle){
              return handle !== "";
            })
            socials = socials.map(function(handle){
              return handle.split(":")
            })
            if (socials[0][1] != ""){
              for (handle in socials){
                let row = document.createElement("tr");
                let head = document.createElement("th");
                head.innerText = socials[handle][0];
                let data = document.createElement("td");
                data.innerText = socials[handle][1];
                row.appendChild(head);
                row.appendChild(data);
                contacts.appendChild(row);
              }
            }
        }
    };
  xhttp.open("GET", "/getSocials?user=" + username, true);
  xhttp.send();
}

// AJAX retrieves hobbies
let retrieveHobbies = function(){
  let hobbyList = document.getElementById("hobby-list")
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let hobbies = this.responseText.split(",");
            hobbies = hobbies.filter(function(hobby){
              return hobby != ""
            })
            for (hobby in hobbies){
              let child = document.createElement("li");
              child.innerText = hobbies[hobby];
              hobbyList.appendChild(child);
            }
        }
    };
  xhttp.open("GET", "/getHobbies?user=" + username, true);
  xhttp.send();
}


retrieveSocials();
retrieveHobbies();
