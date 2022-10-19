const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  let nums = line.split(" ").map((num) => parseInt(num));
  let a, b;
  a = nums[0];
  b = nums[1];
  if (a > b) {
    console.log(">");
  } else if (a === b) {
    console.log("==");
  } else {
    console.log("<");
  }
  rl.close();
}).on("close", function () {
  process.exit();
});
