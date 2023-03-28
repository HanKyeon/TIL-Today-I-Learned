/*
에디터

L은 커서를 왼 쪽으로 한 칸 옮긴다. 맨 앞이면 무시.
D는 우측으로 한 칸 무시. 맨뒤면 무시.
B는 왼쪽 문자 삭제. 맨 앞이면 무시.
P $ 는 $ 문자를 커서 왼쪽에 추가.
초기 문자여르, 이후 입력 문자열 제시. 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구해라.

입력
초기 문자열. 길이 n, 영어 소문자, 100000 이하.
명령 갯수 M 제시.
m개 줄 명령어 제시.
*/
const readline = require("readline")
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

let cnt = -1
let lstk = null
let rstk = []
function ordering(order) {
  switch (order) {
    case "L":
      if (lstk.length) {
        rstk.push(lstk.pop())
      }
      break
    case "D":
      if (rstk.length) {
        lstk.push(rstk.pop())
      }
      break
    case "B":
      if (lstk.length) {
        lstk.pop()
      }
      break
    default:
      lstk.push(order[order.length - 1])
      break
  }
}

rl.on("line", (line) => {
  if (lstk === null) {
    lstk = [...line]
    return
  }
  if (cnt === -1) {
    cnt = parseInt(line)
    return
  }
  ordering(line)
  cnt -= 1
  if (cnt === 0) {
    rl.close()
  }
}).on("close", () => {
  console.log(lstk.join("") + rstk.reverse().join(""))
})

// let pointer = 0
// let mzy = null
// const ordering = function (order) {
// switch (order) {
//   case "L":
//     if (pointer > 0) {
//       pointer -= 1
//     }
//     break
//   case "D":
//     if (pointer < mzy.length) {
//       pointer += 1
//     }
//     break
//   case "B":
//     if (pointer > 0) {
//       mzy.replace(mzy[pointer - 1])
//     }
//     break
//   default:
//     mzy = mzy.slice(0, pointer) + order[order.length - 1] + mzy.slice(pointer)
//     pointer += 1
//     break
// }
// }

// rl.on("line", function (line) {
//   if (mzy === null) {
//     mzy = line
//     pointer = mzy.length
//     return
//   }
//   if (cnt < 0) {
//     cnt = parseInt(line)
//     return
//   }
//   ordering(line)
//   cnt -= 1
//   if (cnt === 0) {
//     rl.close()
//   }
// }).on("close", function () {
//   console.log(mzy)
// })
