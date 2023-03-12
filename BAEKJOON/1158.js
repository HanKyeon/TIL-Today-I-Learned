/*
요세푸스 문제

1번부터 n명의 사람이 원을 이루며 앉아있고, 양의 정수 k가 주어진다.
순서대로 k번째 사람을 제거하는 것을 반복한다. 모두 제거 될 때까지.
제거되는 순서를 N-K 요세푸스 순열이라고 한다.
7, 3의 경우 3 6 2 7 5 1 4 이다.

입력
n, k 제시.

출력
<요세푸스 순열>
*/
// +
const readline = require("readline")
const process = require("process")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
let nk
rl.on("line", (line) => {
  nk = line.split(" ").map((el) => parseInt(el))
  rl.close()
}).on("close", function () {
  let n, k
  n = nk[0]
  k = nk[1] - 1
  let nl = []
  for (i = 1; i <= n; i++) {
    nl.push(i)
  }
  let p = k
  let ans = ``
  cnt = 0
  while (cnt !== n) {
    cnt += 1
    p %= nl.length
    nl = nl.filter((num, idx) => {
      if (idx === p) {
        if (ans === ``) {
          ans += `${num}`
          return false
        }
        ans += `, ${num}`
        return false
      }
      return true
    })
    p += k
  }
  console.log(`<${ans}>`)
})
