// ex 1
let elememt = document.getElementById("navBar")
elememt.setAttribute("id", "socialNetworkNavigation");


let newLi = document.createElement("li");
console.log(newLi);
let textNode = document.createTextNode("Logout");
newLi.appendChild(textNode);
let ul = document.getElementsByTagName("ul")[0];
ul.appendChild(newLi);
let firstLi = ul.firstElementChild;
let lastLi = ul.lastElementChild;
console.log(firstLi.textContent, lastLi.textContent);

//ex 1.b
// let myList = document.createElement("li");
// myList.innerHTML = "Logout";
// document.getElementsByTagName("ul").appendChild(myList);

    // let ul = document.getElementsByTagName("ul")
    // let li = document.createElement("li");
    // li.appendChild(document.createTextNode("Logout"));
    // document.ul.appendChild = "li"

// let newLi = document.createElement("LI");
// document.getElementsByTagName("UL").appendChild(newLi); 




