let boxes = document.querySelectorAll(".box");
let reset_btn = document.querySelector("#reset");
let new_btn = document.querySelector("#new_game");
let msg_container = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");
    // 2 players playerO and playerX
let playerO = true;
    //  winning possibilities
const winning = [
    [0,1,2] , [3,4,5] , [6,7,8] ,
    [0,3,6] , [1,4,7] , [2,5,8] ,
     [0,4,8] , [2,4,6]
];
// reset button
const resetGame  = () =>
{
    playerO = true;
    enablebox();
    console.log("The game is starting again");
} 
//    adding events
boxes.forEach((box) => {
box.addEventListener("click", () =>{
    console.log("box was clicked");
       //adding an inner text with every click
       if (playerO) {
            box.innerText = "O";
            playerO = false;
       }
       else{
        box.innerText = "X";
        playerO = true;
       }
       box.disabled = true;
       checkWinner();
});
});
    const disablebox = () =>
    {
        for(let box of boxes){
            box.disabled = true;
        }
    }
    const enablebox = () =>
    {
        for(let box of boxes){
            box.disabled = false;
            box.innerText = "" ;
            msg_container.classList.add("hide");
        }
    }
const showWinner = (winner) =>
{
   msg.innerText = 'HURRAY!, YOU WON ';
   msg_container.classList.remove("hide");
   disablebox();
}

// checking the winner now 

const checkWinner = () =>
{
    for( let pattern of winning) {
        let pos0 = boxes[pattern[0]].innerText;
        let pos1 = boxes[pattern[1]].innerText;
        let pos2 = boxes[pattern[2]].innerText;

       if (pos0 != "" && pos1 != "" && pos2 != "") {
        if (pos0===pos1 && pos1 === pos2) {
            console.log("WINNER!!" , pos0);
            showWinner(pos0);
        }
       }
    }
}
new_game.addEventListener("click" , resetGame);
reset.addEventListener("click" , resetGame);