// forEach-----------------------------------------------------------------
const colors = ["red", "blue", "green"];

const printClr = function (color) {
  console.log(color);
};
colors.forEach(printClr);

colors.forEach((color) => console.log(color));

// map-----------------------------------------------------------------

const nbz = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const nb2 = function (num) {
  return num * 2;
};
console.log(nbz.map(nb2));
console.log(nbz);
console.log(nbz.forEach(nb2)); // 얘는 적용이 되지는 않는다.
console.log(nbz); // 그래서 바뀌지 않음

const newArray = nbz.map((num) => {
  return num * 2;
});
const newArray2 = nbz.map((num) => num * 2);
console.log(newArray);
console.log(newArray2);

// filter-----------------------------------------------------------------
const products = [
  { name: "cucumber", type: "vegetable" },
  { name: "banana", type: "fruit" },
  { name: "carrot", type: "vegetable" },
  { name: "apple", type: "fruit" },
];
const fruitFillter = function (product) {
  return product.type === "fruit";
};
const newProducts = products.filter(fruitFillter);

console.log(newProducts);
console.log(
  nbz.filter((num) => {
    return num % 2; // 자동 형변환 되어서 홀수만 남음.
  })
);
console.log(
  products.filter((product) => {
    return product.type === "fruit";
  })
);

// reduce-----------------------------------------------------------------

const nbs = [90, 80, 70, 100];

// 총합
const sumNumer = nbs.reduce(function (result, num) {
  return result + num;
}, 0);
console.log(sumNumer);
// 평균
const avgNum =
  nbs.reduce(function (result, num) {
    return result + num;
  }, 0) / nbs.length;
console.log(avgNum);

// find----------------------------------------------------------------
const avengers = [
  { name: "Tony Stark", age: 45 },
  { name: "Steve Rogers", age: 32 },
  { name: "Thor", age: 40 },
];

const avenger = avengers.find((avenger) => {
  return avenger.name === "Tony Stark";
});
console.log(avenger);

// some----------------------------------------------------------------
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const someArr = arr.some((num) => {
  return num % 2;
});
console.log(someArr);

// every----------------------------------------------------------------
const everyArr = arr.every((num) => {
  return num % 2;
});
console.log(everyArr);

let a = [1, 2, 3];
let b = a;
console.log([1, 2, 3] == [1, 2, 3]); // false
console.log(a == [1, 2, 3]); // false
console.log(a == b); // true
console.log(a === b); // true
console.log([1, 2, 3] === [1, 2, 3]); // false

let prac = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
prac.forEach((num, idx) => {
  if (idx >= 1) {
    prac[idx] = num + prac[idx - 1];
  }
});
console.log(prac);

// 가능은 하나 코드의 시작을 괄호로 하면 혼쭐낸다.
[1, 2, 3].forEach((num) => {
  console.log(num);
});
