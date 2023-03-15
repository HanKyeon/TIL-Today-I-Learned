/*
균형잡힌 세상

() [] 있다. 1대 1 매칭해라.

입력
입력 종료 조건은 온점 하나. 나머지는 100글자 이하 문자열

출력
균형잡혀 있다면 yes 아니라면 no
*/
const readline = require("readline")
const rl = readline.Interface({
  input: process.stdin,
  output: process.stdout,
})

let ansList = []

rl.on("line", function (line) {
  if (line === ".") {
    rl.close()
    return
  }
  let ans = "yes"
  let stk = []
  for (let char of line) {
    if (char === "(") {
      stk.push(char)
      continue
    } else if (char === ")") {
      if (stk.length !== 0 && stk[stk.length - 1] === "(") {
        stk.pop()
        continue
      } else {
        ans = "no"
        break
      }
    } else if (char === "[") {
      stk.push(char)
    } else if (char === "]") {
      if (stk.length !== 0 && stk[stk.length - 1] === "[") {
        stk.pop()
        continue
      } else {
        ans = "no"
        break
      }
    } else {
      continue
    }
  }
  if (stk.length !== 0) {
    ans = "no"
  }
  ansList.push(ans)
}).on("close", function () {
  ansList.forEach((val) => {
    console.log(val)
  })
})
