let yourScore = 0;
let compScore = 0;
const msg = document.querySelector("#msg");
const choices = document.querySelectorAll(".choice");
let userScore = document.querySelector("#you");
let comScore = document.querySelector("#comp");
const GencompChoice = () =>
{
     const options= ["rock" , "paper"  , "scissor"];
    //  math.random() is use to pick  number b/w 0-1 but in oder to pick a higher number we do        Math.random() *desired_num+1  , here:- Maths.random() *3 {3 for picking number b/w 0 to 2}
    // but it gives decimal values too so in order to remove them we use :- Math.floor(Math.random() *3)
   const randIdx =  Math.floor(Math.random()*3);
   return options[randIdx];
}
showWinner = (userWin) =>
{
  if (userWin) {
    // console.log("HURRAY!, You win");
    // score updation
    yourScore++;
    userScore.innerText = yourScore;
    msg.innerText = "HURRAY!, You win";
    msg.style.backgroundColor = 'green'; 
  }
  else{
    // console.log("OOPS!, You loss");
    compScore++;
    comScore.innerText = compScore;
    msg.innerText = "OOPS!, You loss";
    msg.style.backgroundColor = 'red'; 
  }
}
const drawGame = () =>
{
    // console.log("The game is Draw!");
    msg.innerText = "Game is draw , Play Again";
    msg.style.backgroundColor = 'brown'; 
}
const playGame = (userChoice )=>
{
    console.log("user choice = " , userChoice);
    // generating comp choice
    const compChoice = GencompChoice();
    console.log("comp choice = " , compChoice);

    if (userChoice === compChoice) {
        drawGame();
    } else{
        let userWin = true;
        if (userChoice == "rock") {
            // paper, scissor
            userWin= compChoice ==="paper" ?false : true;
        } else if (userChoice == "paper") {
            // rock , scissor
            userWin = compChoice === "rock"?true : false;
        } else{
            // rock , paper
            userWin = compChoice ==="rock" ?false:true;
        }
        showWinner(userWin);
    }
}

choices.forEach((choice) => {
    console.log(choice);
   choice.addEventListener("click" , () =>
   {
    const userChoice = choice.getAttribute("id");
   playGame(userChoice);
   })
})