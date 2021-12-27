var arr = []; // define our array
for (var i = 0; i < 3; i++) { // loop 3 times
    arr.push(prompt('Enter a word ' + (i + 1))); // push the value into the array
}
function frame(arr) {
    let max_length = arr.reduce((a, b) => a.length > b.length ? a : b).length;
    let border = '*'.repeat(max_length + 4)
    let ret = border + "\n"
    arr.forEach(element => {
        let currentRow = `* ${element}`
        while (currentRow.length < max_length + 3) currentRow += " "
        currentRow += "*"
        ret += `${currentRow}\n`
    });
    ret += border
    return ret
}
console.log(frame(arr))