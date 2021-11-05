const timerSpan  = document.querySelector(`#timer`)
let timer = 10
let interval = setInterval(() => {
    timer--
    timerSpan.textContent = timer
    // if(timer===0){
    //     clearInterval(interval)
    // }
}, 1000);

let incrementXYPostion = 0
const redCube = document.querySelector("#red")
let incrementInterval= ()=>{let currentInterval  = setInterval(() => {
    redCube.style.top=`${incrementXYPostion}px`
    redCube.style.left=`${incrementXYPostion}px`
    incrementXYPostion+=50
    if(incrementXYPostion==500){
        clearInterval(currentInterval)
        incrementXYPostion = 0
    }
}, 500)};
let starter = document.querySelector(`#starter`)
starter.addEventListener('click', incrementInterval);

