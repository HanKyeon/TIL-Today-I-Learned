// console.log("hello world");
// if (isClean) {
//   console.log("clean!");
// }
// let ramen = 1;

function add(num1, num2) {
  return num1 + num2;
}
console.log(add(2, 7));

const sub = function (num1, num2) {
  return num1 - num2;
};
console.log(sub(2, 7));

const greeting = function (name = "Annonymous") {
  return `Hi ${name}`;
};
console.log(greeting());

const greeting2 = (name = "가능?") => {
  return `hello, ${name}`;
};
const greeting3 = (name) => {
  return `hello, ${name}`;
};
const greeting4 = (name) => `hello, ${name}`;

let parts = ["shoulders", "knees"];
let lyrics = ["head", ...parts, "as"];
console.log(lyrics);

const rest0pr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, ...restArgs];
};
console.log(rest0pr(1, 2, 3, 4, 5, 6)); // 이것도 가능
console.log(greeting2());

const numbers = [1, 2, 3, 4, 5];
console.log(numbers[0]);
console.log(numbers[numbers.length - 1]);

numbers.reverse();
console.log(numbers);

numbers.push(100);
console.log(numbers);
numbers.pop();
console.log(numbers);

numbers.unshift(100);
console.log(numbers);
numbers.shift(100);
console.log(numbers);

console.log(numbers.includes(100));
console.log(numbers.includes(1));

console.log(numbers.indexOf(1));
console.log(numbers.indexOf(100));

console.log(numbers.join(""));
console.log(numbers.join());
