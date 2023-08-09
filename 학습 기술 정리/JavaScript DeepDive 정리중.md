# JavaScript Deep Dive 정리

학습 후기 : **기본적인 JS의 문법과 mdn을 참고한 메서드 정리 등은 패스하고, 개인적으로 JS가 어떤 식으로 동작하는지 학습하고 싶었기에 JS에 대한 총체적인 정리는 pass하고 JS Deep Dive 책을 통해 학습한 내용을 정리 예정. 기타 JS의 특별한 비동기 및 클로저 등 여러 개념들 역시 함께 정리 할 것이다.**

## WHY?

## WHAT?

- 클로저
- 일급 객체
- async await vs then chaining
- this
- 상속
- 프로토타입

## HOW?

## WHAT IF?

---

### in vs hasOwnProperty vs ?.(optional chaining operator)

- `?.`은 `property`의 값을 가져온다.
- `in`과 `hasOwnProperty`는 해당 `key`의 유무를 확인한다.
- `hasOwnProperty`는 해당 객체만 가진 `property`만 확인한다.
- `in`은 `__proto__`를 통해 상속한 `key`의 유무까지 확인한다.
