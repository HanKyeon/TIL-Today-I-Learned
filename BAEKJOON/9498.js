/*
시험 성적

점수를 입력 받아 90~100은 A 80~89는 B, 70~79는 C, 60~69는 D 나머지는 F 출력
*/

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  let num = parseInt(line);
  if (90 <= num && num <= 100) {
    console.log("A");
  } else if (80 <= num && num < 90) {
    console.log("B");
  } else if (70 <= num && num < 80) {
    console.log("C");
  } else if (60 <= num && num < 70) {
    console.log("D");
  } else {
    console.log("F");
  }
  rl.close();
}).on("close", function () {
  process.exit();
});
