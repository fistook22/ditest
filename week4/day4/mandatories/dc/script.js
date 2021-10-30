let word = "bottles";
let count = 99;
let fall = 1;
while (count > 0) {
    if (count == 1) {
        let word = "bottle"
    }
    console.log(count + " " + word + " of beer on the wall");
    console.log(count + " " + word + " of beer,");
    console.log("Take" + " " + fall + " down, pass it around,");
    count = count - fall;
    fall = fall + 1;
    if (count > 0) {
        if (count == 1) {
            let word = "bottle"
        }
        console.log(count + " " + word + " of beer on the wall.");
    } else {
        if (count < 1) {
            let word = "bottles"
        }
        console.log("No more " + word + " of beer on the wall.");
    }
}