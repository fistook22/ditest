let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

console.log(users.length)
if(!users.length){
    console.log("no one online")
}else if(users.length===1){
    console.log(users[0]+"is online")
}else if(users.length===2){
    console.log(users[0]+"and"+users[1]+"is online")
}else{
    console.log(users[0]+" and "+users[1]+" and more "+(users.length-2)+"are on line")
}