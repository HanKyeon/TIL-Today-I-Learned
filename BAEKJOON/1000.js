/*
1000번

A + B 출력
*/
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

var rs = 0;

rl.on("line", (line) => {
  input = line.split(" ").map((el) => parseInt(el)); // 1 2 3 4
  rl.close();
});

rl.on("close", () => {
  input.forEach((el) => {
    rs += el;
  });
  console.log(rs);
  process.exit();
});

// const fs = require("fs");
// const inputData = fs.readFileSync("/dev/stdin").toString().split(" ");

// const a = parseInt(inputData[0]);
// const b = parseInt(inputData[1]);

// console.log(a + b);
