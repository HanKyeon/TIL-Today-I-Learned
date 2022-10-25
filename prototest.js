let cat = {
  name : '메롱',
  age : 5,
  attack: function () {
    console.log(`${this.name} 공격~`)
  }
}

let kitty = {
  haha : 'ㅎㅎ',
}

kitty.__proto__ = cat

console.log(kitty.attack())