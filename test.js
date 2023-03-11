console.log(`         ,r'"7`)
console.log("r`-_   ,'  ,/")
console.log(` \\. ". L_r'`)
console.log("   `~\\/")
console.log(`      |`)
console.log(`      |`)

const test = async function () {
  console.log("async 함수 처리")
  return { data: "반환 값 /" }
}
console.log(
  test().then((res) => {
    console.log(res.data, "응답 데이터 실행")
  })
)
/*
=> 아래 입력이 찍힌다.
=> 순서대로 async 함수 처리가 된 뒤, test.then() 출력 이후 then 내부 데이터 실행.
=> 음.... 내 생각엔 내부 함수가 먼저 실행된 뒤 test.then()이 출력되야 하는 것 같은데 왜 이 순서로 출력이 될까?

async 함수 처리
Promise { <pending> }
반환 값 / 응답 데이터 실행
*/

// let a = [0,1,2,3,4]
// let n = 5
// a.forEach((num) => {
//   const oneLine = []
//   for (let i = 1; i < 5-num; i++) {
//     oneLine.push(' ')
//   }
//   for (let i = 0; i < num; i++) {
//     oneLine.push('*')
//   }
//   oneLine.push('*')
//   for (let i = 0; i < num; i++) {
//     oneLine.push('*')
//   }
//   for (let i = 1; i < 5-num; i++) {
//     oneLine.push(' ')
//   }
//   console.log(oneLine.join(""))
// })
