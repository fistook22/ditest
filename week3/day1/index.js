//this is my first javascript code
console.log('hello world');

let addressNumber = '49';
let addressStreet = 'nachalat benyamin';
let country = 'israel';
let globalAddress = addressNumber + " " + addressStreet + " " + country;
console.log(globalAddress);

let text1 = "i will be";
let text2 = "in";
let birthYear = 1991;
birthYear.toString();
let futureYear = 2025;
futureYear.toString();
console.log(text1 + " " + (futureYear - birthYear) + " " + text2 + " " + futureYear)

let pets = ['cat', 'dog', 'fish', 'rabbit', 'cow'];
let favourite = pets[1];
console.log(favourite)
pets.splice(3, 1, 'horse')
console.log(pets)
console.log(pets.length)



let isBoss = confirm("Are you the boss?");
alert(isBoss); // true if OK is pressed