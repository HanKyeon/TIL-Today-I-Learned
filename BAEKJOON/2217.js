/*
로프

n개의 로프가 있다. k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, w/k만큼 중량이 걸린다.
각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내시오. 모든 로프 쓸 필요 없고, 몇개만 골라도 됨.

입력
n 제시.
n개 줄 로프가 버틸 수 있는 최대 중량 제시. 10000을 넘지 않는 자연수.

출력
답 출력
*/

const readline = require("readline")
const rl = readline.Interface({
  input: process.stdin,
  output: process.stdout,
})

let n = null
let nl = []

rl.on("line", function (line) {
  if (!n) {
    n = parseInt(line)
    return
  }
  nl.push(parseInt(line))
  if (nl.length === n) {
    rl.close()
  }
}).on("close", function () {
  nl.sort(function (a, b) {
    return b - a
  })
  let ropeCnt = 0
  let ans = 0
  nl.forEach((val) => {
    ropeCnt += 1
    if (val * ropeCnt > ans) {
      ans = val * ropeCnt
    }
  })
  console.log(ans)
})
