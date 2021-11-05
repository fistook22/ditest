let h1 = document.getElementById("header");
console.log(h1.textContent);

let lastElem = document.getElementById("lastElem");
lastElem.remove();

let h2 = document.getElementById("h2");
document.getElementById('h2').onclick = changeColor;

function changeColor() {
    h2.style.color = "red";
}

let h3 = document.getElementById("h3");
h3.addEventListener("click", (e) => {
    h3.style.display = "none";
})

// let article = document.getElementsByTagName("article");
// let button = document.getElementsByTagName("button");
// button.addEventListener("click", (e) => {
//     article.style.fontWeight = "900";
// })


let btn = document.getElementById("toggleBold");
btn.addEventListener("click", function(){
    let bold = document.querySelectorAll("p");
    for(i = 0; i < bold.length; i ++){
        bold[i].style.fontWeight = "bold";
    }
});
let newP = document.createElement("p");
newP.innerHTML = "this is the new p";
document.querySelector("article").appendChild(newP);