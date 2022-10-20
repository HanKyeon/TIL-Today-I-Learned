

let a = [0,1,2,3,4]
let n = 5
a.forEach((num) => {
  const oneLine = []
  for (let i = 1; i < 5-num; i++) {
    oneLine.push(' ')
  }
  for (let i = 0; i < num; i++) {
    oneLine.push('*')
  }
  oneLine.push('*')
  for (let i = 0; i < num; i++) {
    oneLine.push('*')
  }
  for (let i = 1; i < 5-num; i++) {
    oneLine.push(' ')
  }
  console.log(oneLine.join(""))
})



