// const readline = require("readline");

// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });

// var rs = 0;

// rl.on("line", (line) => {
//   input = line.split(" ").map((el) => parseInt(el)); // 1 2 3 4
//   rl.close();
// });

// rl.on("close", () => {
//   input.forEach((el) => {
//     rs += el;
//   });
//   console.log(rs);
//   process.exit();
// });

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let nums;

rl.on("line", (line) => {
  nums = line.split(" ").map((el) => parseInt(el));
  rl.close();
});

rl.on("close", () => {
  let a, b;
  a = nums[0];
  b = nums[1];
  console.log(a / b);
});
