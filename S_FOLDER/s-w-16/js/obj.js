const myInfo = {
  name: "jack",
  phoneNumber: "123456",
  "samsung product": {
    buds: "Buds pro",
    galaxy: "S99",
  },
};

console.log(myInfo.name);
console.log(myInfo.phoneNumber);
console.log(myInfo["samsung product"].buds);
console.log(myInfo["samsung product"].galaxy);

for (const i in myInfo) {
  if (myInfo.hasOwnProperty.call(myInfo, i)) {
    const element = myInfo[i];
    console.log(element);
    console.log(i);
  }
}

const obj = {
  greeting() {
    console.log("hihi");
  },
};
console.log(obj.greeting());

const key = "country";
const value = ["한", "중", "일", "미"];

const myObj = {
  [key]: value,
};

console.log(myObj);
console.log(myObj.country);

const userInfo = {
  name: "ssafy kim",
  userId: "ssafyStudent1234",
  phoneNumber: "010-1234-1234",
  email: "ssafy@ssafy.com",
};

// const {name} = userInfo
// const {userId} = userInfo
const { phoneNumber } = userInfo;
const { email } = userInfo;
// 여러개 할당 가능
const { name, userId } = userInfo;
console.log(name);
console.log(phoneNumber);
console.log(email);
console.log(userId);
// const name = userInfo.name
// const userId = userInfo.userId
// const phoneNumber = userInfo.phoneNumber
// const email = userInfo.email

// JSON 변환하기
const jsonData = {
  coffee: "Ame",
  icecream: "Cookie & Cream",
};

// Obj -> json
const obj2Json = JSON.stringify(jsonData);
console.log(obj2Json);

// json -> Obj
const json2Obj = JSON.parse(obj2Json);
console.log(json2Obj);
console.log(json2Obj.coffee);

// 타입 비교
console.log(typeof obj2Json); // str
console.log(typeof json2Obj); // obj
