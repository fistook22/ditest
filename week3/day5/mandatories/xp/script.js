// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .


//ex1
// let colors = ["blue", "red", "green", "yellow"];
// for (let i = 0; i < colors.length; i++) {
//     console.log("my #" + [i] + " " + "choice is" + " " + colors[i]);
// }


// Write code to remove “Greg” from the people array.

// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.

// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop. Hint: take a look at the break statement in the lesson.

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name. Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1 ?

// Create a variable called last which value is the last element of the array.



// //ex2
// let people = ["Greg", "Mary", "Devon", "James"];
// people.shift();
// people.splice(2, 1, "Jason", "Shai");
// for (let i = 0; i < people.length; i++) {
//     console.log(people[i]);
//     if (i === 2) { break; }
// }
// let myPeople = people.slice(1, -1);
// console.log(myPeople);
// console.log(people.indexOf("Mary"));
// console.log(people.indexOf("Foo"));
// let last = people[people.length - 1];
// console.log(last);




//Prompt the user for a number.
// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)



//ex3
// let num = prompt("please submit a number");
// while (num < 10) {
//     num++;
// }   //  ??? ask dan


//ex4

let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor +
    building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0]);
let sum = building.numberOfRoomsAndRent.sarah[1] +
    building.numberOfRoomsAndRent.david[1];
if (sum > building.numberOfRoomsAndRent.dan[1]) {
    let (building.numberOfRoomsAndRent.dan) = [4, 1200]
}