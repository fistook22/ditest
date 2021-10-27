function feedArray(numberOfWord) {
    let arrayOfWords = []
    for (let index = 0; index < numberOfWord; index++) {
        arrayOfWords.push(prompt("whats your next word?"))

    }
    return arrayOfWords
}

function createTheFrame(array) {
    let toDisplay = ''
    let longest = array.reduce((a, b) => {
        return a.length > b.length ? a.length : b.length;
    }
    );
    while (toDisplay.length < longest + 4) toDisplay += "*"
    toDisplay += '\n';
    for (let index = 0; index < array.length, index++;) {
        let toAdd = ""
        toAdd += '* '
        const element = array[index];
        toAdd += "${element}"
        while (toAdd.length < longest + 3) toAdd += ' '
        toAdd += '*\n'
        toDisplay += toAdd
    }
    let toAdd = ''
    while (toAdd.length < longest + 4) toAdd += "*"
    toDisplay += toAdd
    console.log(toDisplay)
}
createTheFrame(feedArray(prompt("how many word in the frame?")))