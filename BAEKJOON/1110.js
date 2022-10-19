const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (num) => {
  let n = parseInt(num);
  let o;
  let i = 0;
  while (true) {
    i++;
    o = Math.floor(n / 10) + (n % 10);
    n = (n % 10) * 10 + (o % 10);
    if (n === parseInt(num)) {
      break;
    }
  }
  console.log(i);
  rl.close();
}).on("close", function () {
  process.exit();
});
