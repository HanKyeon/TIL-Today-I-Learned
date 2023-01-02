let cat = {
  name: "메롱",
  age: 5,
  attack: function () {
    console.log(`${this.name} 공격~`)
  },
}

/**
 * 고양이 객체
 * @todo 뭐 더 해야합니다.
 * @see 링크 달아서 할 수도 있고
 * @type {object}
 */
let kitty = {
  haha: "ㅎㅎ",
}

/**
 * 키티의 haha를 출력하는 함수
 * @version 버전명시가능
 * @deprecated 다른 거 써주세요 할 때 사용. 사용 시 줄 그어짐
 * @param {object} kitty 키리 객체
 * @returns 고양이 웃음소리 반환
 */
function update(kitty) {
  console.log(kitty.haha)
}
update(kitty)
kitty.__proto__ = cat

console.log(kitty.attack())
