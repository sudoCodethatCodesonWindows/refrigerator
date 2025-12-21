const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

let board = Array.from({length:3},()=>Array(3).fill(" "));
let player = "X";

function printBoard() {
  board.forEach((r,i)=>{
    console.log(" " + r.join(" | "));
    if(i<2) console.log("---+---+---");
  });
}

function win(p) {
  for(let i=0;i<3;i++)
    if(board[i].every(c=>c===p) || board.map(r=>r[i]).every(c=>c===p))
      return true;
  return [0,1,2].every(i=>board[i][i]===p) ||
         [0,1,2].every(i=>board[i][2-i]===p);
}

function draw() {
  return board.flat().every(c=>c!==" ");
}

function ask() {
  printBoard();
  rl.question(`\nPlayer ${player} (row col or q): `, ans=>{
    if(ans==="q") return rl.close();
    let [r,c]=ans.split(" ").map(Number);
    if(!r||r<1||r>3||c<1||c>3||board[r-1][c-1]!==" ") {
      console.log("Invalid move!");
      return ask();
    }
    board[r-1][c-1]=player;
    if(win(player)) { printBoard(); console.log(`${player} wins!`); return rl.close(); }
    if(draw()) { printBoard(); console.log("Draw!"); return rl.close(); }
    player = player==="X"?"O":"X";
    ask();
  });
}

ask();
