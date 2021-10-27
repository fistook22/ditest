function playTheGame() {
    let play = confirm("would you like to play a game?");
    if (play != true) {
        alert("No problem, Goodbye");
       }else{
            let userNumber = prompt("Choose a number");
            let tries = 1++;
            if (typeof userNumber != "number") {
                alert("Sorry this is not a number, Goodbye");
                if (userNumber < 0 && userNumber >10) {
                    alert("Sorry it's not a good number, goodbye");
                }else{
                    let computerNumber = Math.floor(Math.random() * 11);
                }
            }
        }
    }
playTheGame()

function test(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
        alert("Winner!");
        if (userNumber > computerNumber) {
            userNumber = prompt("Your number is bigger then the computer’s, guess again");
            if (userNumber < computerNumber) {
                userNumber = prompt("Your number is smaller then the computer’s, guess again");
            }else if (tries >= 3) {
                return alert("Out of chances")
            }
        }
    }
}