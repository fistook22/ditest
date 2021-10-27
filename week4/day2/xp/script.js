//ex 1
// function infoAboutMe() {
//     console.log("my name is shai, i am 30 years old amd i love surfing and snowboarding")
// }
// infoAboutMe()

// function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies=[]) {
// console.log("your name is" + " " + personName + "," + " " + "you are" + personAge + "years old" + "," + "your favorite color is" + " " + personFavoriteColor);
// console.log(`your name is ${personName}, you are ${personAge}, your favorite color is ${personFavoriteColor}`);
// personHobbies.forEach(hobby => console.log(hobby));
// }

// infoAboutPerson("david", 45, "blue");
// infoAboutPerson("josh", 12, "yellow");

// infoAboutPerson("David", 45, "blue", ["tennis", "painting"]);
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])


//ex 2
// let age = undefined
// function checkDriversAge(age) {
//     console.log(age);
//     if (!age) {
//         age = parseInt(prompt("How old are you?"));
//     }
//     if (typeof age != "number") {

//         return checkDriversAge(parseInt(prompt("that is not a number")));
//     }
//     if (age < 18) {
//         alert("Sorry, you are too young to drive this car. Powering off");
//     } else if (age > 18) {
//         alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     } else {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
// }


// checkDriversAge()


//ex 3
// let i = undefined;
// function checkNumber() {
//     for (let i = 0; i < 101; i++) {
//         console.log(i);
//         if (i % 2 == 0) {
//             console.log("The number is even.");
//         } else {
//             console.log("The number is odd.");
//         }
//     }
// }
// checkNumber();


//ex 4
// function calculator(bill) {
//     let factor = 0.2
//     if (bill > 50) {
//         factor -= 0.05
//     }
//     if (bill > 200) {
//         factor -= 0.15
//     }
//     let tipAmount = (bill * factor).toFixed(2)
//     let finalBill = bill + tipAmount
//     console.log(tipAmount)
//     console.log(finalBill)
// }
// calculator(160)



//ex5

function hotelCost(numberNights) {
    numberNights = parseInt(numberNights)
    let hotelCost = 140
    if (isNaN(numberNights)) {
        return hotelCost()
    } else {
        return hotelCost *= numberNights
    }
}‏

function planeRideCost(dest) {
    dest = dest.toLowerCase()
    switch (dest) {
        case "london":
            planeCost = 183
            break;
        case "paris":
            planeCost = 220
            break;
        case "":
            planeCost = false
            break;

        default:
            planeCost = 300
            break;
    }
    return planeCost
}‏

function rentalCarCost(dayRent) {
    dayRent = parseInt(dayRent)
    if (isNaN(dayRent)) {
        return dayRent * 40
    } else {
        return dayRent < 10 ? dayRent * 40 : dayRent * 40 * 0.95
    }
}

(function totalVacationCost() {
    let totalSteps = [
        [hotelCost, "how many nights will you stay?"],
        [planeRideCost, "where do you want to go?"],
        [rentalCarCost, "how many days will you rent the car?"]
    ], totalAmount = 0, lastVal

    totalSteps.forEach((element[0](prompt(element[1]))))
    do {
        lastVal = element[0](prompt(element[1]))
    } while (lastVal == false);
    console.log(lastVal)
    totalAmount += lastVal
console.log(totalAmount)
return totalAmount
})