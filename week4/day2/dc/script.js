var arr = []; // define our array

for (var i = 0; i < 3; i++) { // loop 3 times
    arr.push(prompt('Enter a word ' + (i + 1))); // push the value into the array
}

str = arr.join("")

function frame(str) {
    let lines = str.split('\n')
        // get length of longest line:
    let max_length = Math.max(...lines.map(l => l.length))
    let border = '*'.repeat(max_length + 4)

    let ret = border + "\n"
        // make inner lines padded to length:
    ret += lines.reduce((s, l) => s += `* ${l.padEnd(max_length)} *\n`, "")
    ret += border
    return ret
}

console.log(frame(str))