const queryKeys = {
  ////////////
  /* 최상단 */
  ////////////
  user: () => [`user`],
  scene: (taleId, sceneOrder) => [...queryKeys.user(), taleId, sceneOrder], // 최상단

  ///////////////
  /* user 하위 */
  ///////////////
  game: () => [...queryKeys.user(), `game`],
  store: () => [...queryKeys.user(), `store`],

  ///////////////
  /* game 하위 */
  ///////////////
  progress: () => [...queryKeys.game(), `progress`],
  play: () => [...queryKeys.game(), `play`],

  ///////////////////
  /* progress 하위 */
  ///////////////////
  progressList: () => [...queryKeys.progress(), `list`],
  progressDetail: (taleId) => [...queryKeys.progress(), `detail`, taleId],

  ///////////////////
  /* play 하위 */
  ///////////////////
  playList: () => [...queryKeys.play(), `list`],
  playDetail: (taleId) => [...queryKeys.play(), `detail`, taleId],

  ////////////////
  /* store 하위 */
  ////////////////
  storeList: () => [...queryKeys.store(), `list`],
  storeDetail: (taleId) => [...queryKeys.store(), `detail`, taleId],
  reviewList: (taleId) => [...queryKeys.storeDetail(taleId), `reviews`],
}

console.log("")
console.log(
  queryKeys.user(),
  "queryKeys.user() : 로그인, 로그아웃, 회원정보 수정, 결제 성공 시 invalidate"
)
console.log(queryKeys.scene(404, 405), "queryKeys.scene(404, 405)")
console.log(
  queryKeys.game(),
  "queryKeys.game() : 단어테스트 결과, 스테이지 진행도 저장, "
)
console.log(queryKeys.store(), "queryKeys.store()")
console.log(
  queryKeys.progress(),
  "queryKeys.progress() : 이미지 저장 시 invalidate"
)
console.log(queryKeys.play(), "queryKeys.play()")
console.log(queryKeys.progressList(), "queryKeys.progressList()")
console.log(queryKeys.progressDetail(200), "queryKeys.progressDetail(200)")
console.log(queryKeys.playList(), "queryKeys.playList()")
console.log(queryKeys.playDetail(500), "queryKeys.playDetail(500)")
console.log(
  queryKeys.storeList(),
  "queryKeys.storeList() : review 관련 CRUD 진행 시 invalidate"
)
console.log(queryKeys.storeDetail(204), "queryKeys.storeDetail(204)")
console.log(queryKeys.reviewList(204), "queryKeys.reviewList(204)")
