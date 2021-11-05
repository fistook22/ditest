let form = document.getElementsByTagName("form")[0];
console.log(form);

let input = document.getElementById("fname");
let input1 = document.getElementById("lname");
let input2 = document.getElementById("submit");
console.log(input, input1, input2);

let inputN = document.getElementsByName("fname");
let inputN1 = document.getElementsByName("lname");
let inputN2 = document.getElementsByName("submit");
console.log(inputN, inputN1, inputN2);

// input2.addEventListener("submit", (e)=>{
//     let values = input2.value(input, input1);
// })

form.addEventListener("submit",function101)
function function101(e){
    e.preventDefault()
    let inputValue1 = form.elements[0].value
    let inputValue2 = form.elements[1].value
    if (inputValue1&&inputValue2){
        // let li = document.createElement("li")
        // let textNode = document.createTextNode(`${inputValue1} ${inputValue2}`)
        // li.append(textNode)
        // let ul = document.querySelector("ul")
        // ul.append(li)
        for (let a = 0;a<e.target.elements.length-1;a++){
            let currentInput = e.target.elements[a];
            let li = document.createElement("li")
            let textNode = document.createTextNode(currentInput.value)
            li.append(textNode)
            let ul = document.querySelector("ul")
            ul.append(li)
        }
    }}

