function sayHi(phrase) {
    alert( phrase);
}

clearTimeout(sayHi, 5000, "Sale ends in 10min !");
setTimeout(sayHi, 10000, "Sale ends in 10min !");