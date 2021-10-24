//ex 1

// let x = 5;
// let y = 3;
// if (x > y) {
//     console.log("x is the biggest number");
// }

//ex 2 "chihuahua"
// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’


// let newDog = "chihuahua";
// console.log(newDog.length);
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());
// if (newDog === "chihuahua") {
//     console.log("I love Chihuahuas, it’s my favorite dog breed")
// }
// else {
//     console.log("I dont care, I prefer cats")
// }


//ex 3
// Prompt the user for a number and save it to a variable.
// Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
// let num = prompt ("write a number");
// if (num % 2 == 0) {
//     console.log("num is an even number");
// }
// if (num % 2 == 1) {
//     console.log("num is an odd number");
// }

// //ex 4


let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
console.log(users.length)
if (!users.length) {
    console.log("no one online")
} else if (users.length === 1) {
    console.log(users[0] + "is online")
} else if (users.length === 2) {
    console.log(users[0] + "and" + users[1] + "is online")
} else {
    console.log(users[0] + " and " + users[1] + " and more " + (users.length - 2) + " " + "are online")
}
