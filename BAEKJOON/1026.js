/*
보물

길이가 n인 두 배열 a, b.
s = a[0]*b[0] + ... a[n-1]*b[n-1]
s를 가장 작게 만들기 위해 a의 수 재배열. b는 재배열 x
s의 최솟값출력
n은 50이하 자연수, a,b는 0~100

입력
n
a
b

출력
s 최솟값
*/
const readline = require("readline")
const rl = readline.Interface({
  input: process.stdin,
  output: process.stdout,
})

let n
let a, b
rl.on("line", function (line) {
  if (!n) {
    n = parseInt(line)
    return
  } else if (!a) {
    a = line.split(" ").map((num) => parseInt(num))
    return
  } else if (!b) {
    b = line.split(" ").map((num) => parseInt(num))
    rl.close()
    return
  }
}).on("close", function () {
  a.sort(function (a, b) {
    return a - b
  })
  b.sort(function (a, b) {
    return b - a
  })

  let ans = 0
  for (i = 0; i < n; i++) {
    ans += a[i] * b[i]
  }
  console.log(ans)
})

/**

var inputs = require('fs').readFileSync('/dev/stdin').toString().match(/[^\n$]+/g);

var parser = function (n) {
    return parseInt(n);
};

var sorter = function (a, b) {
    return a - b;
};

var A = inputs[1].split(' ').map(parser).sort(sorter);
var B = inputs[2].split(' ').map(parser).sort(sorter).reverse();

var sum = A.reduce(function (pre, n, i) {
    return pre + n * B[i];
}, 0);

console.log(sum);

 */
