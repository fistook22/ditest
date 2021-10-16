//Ex #1
// let nemo = prompt("write a sentence containing the word Nemo");
// let found = nemo.indexOf("Nemo");
// console.log("I found Nemo at" + " " + found);
// if (found = true) {
//     console.log("Good Job" + "!");
// } else {
//     console.log("I can't find Nemo")
// }

//Ex #1 - Bonus
let nemo = prompt("write a sentence containing the word 'Nemo'");
let found = nemo.indexOf('Nemo');
if (found == -1) {
    console.log("I can't find Nemo");
} else if (found != -1)  {
    console.log("Good Job" + "!")
}