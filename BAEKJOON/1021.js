/*
회전하는 큐

n개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다.
몇 개의 원소를 뽑아낼 것.
1. 첫 번째 원소를 뽑아낸다.
2. 왼쪽으로 한 칸 이동 시킨다.
3. 오른쪽으로 한 칸 이동 시킨다.

큐에 처음 포함되어있던 수 n 제시.
뽑아내려 하는 원소 위치 제시. 주어진 순서대로 뽑아내는데 드는 2,3 연산의 최솟값을 출력해라.

입력
큐 크기 n과 뽑아내려 하는 수 갯수 m 제시. n은 50보다 작거나 같은 자연수
뽑아내려 하는 수의 위치가 순서대로 제시.

출력
2,3 연산 횟수의 최솟값
*/
const readline = require("readline")
const rl = readline.Interface({
  input: process.stdin,
  output: process.stdout,
})

let n, m
let idxList = []

const minus1 = function (val) {
  return val - 1
}
const parser = function (val) {
  return parseInt(val)
}
const sorter = function (a, b) {
  return a - b
}
const leftOrRight = function (target) {
  return target < idxList.length - target - 1
    ? { target }
    : { target: idxList.length - target - 1 }
}

rl.on("line", function (line) {
  nl = line.split(" ").map(parser)
  if (!n) {
    n = nl[0]
    m = nl[1]
    return
  }
  idxList = nl.map(minus1)
  rl.close()
}).on("close", function () {
  idxList.sort(sorter)
  console.log(idxList)
  let ans = 0
  for (i = 0; i < m; i++) {
    const tg = idxList.shift()
    const a = leftOrRight(tg)
    ans += a
    idxList.forEach((val) => val - a)
  }

  console.log(ans)
})

///////////////////////////////////////////////////////

var fs = require("fs")
var input = fs.readFileSync("/dev/stdin").toString().split("\n")
var size = input[0].split(" ")[0]
var num = input[0].split(" ")[1]

var index = new Array()
for (var a = 0; a < num; a++) {
  index[a] = parseInt(input[1].split(" ")[a])
}

var queue = new Array()
for (var a = 0; a < size; a++) {
  queue[a] = a + 1
}

var minimum = 0
for (var a = 0; a < num; a++) {
  var result = new Array()
  result = getMinimum(queue, index[a])
  minimum += result[0]
  queue = result[1]
}
console.log(minimum)
function getMinimum(queue, index) {
  var result = new Array()
  var temp = new Array()
  var target = queue.indexOf(parseInt(index))
  if (queue[0] == index) {
    queue.shift()
    result[0] = 0
    result[1] = queue
    return result
  } else if (queue.length / 2 > target) {
    result[0] = target
    result[1] = queueModify(queue, target, "left")
    return result
  } else {
    result[0] = queue.length - target
    result[1] = queueModify(queue, queue.length - target, "right")
    return result
  }
}

function queueModify(queue, distance, direction) {
  var temp = new Array()
  if (direction == "right") {
    for (var a = 0; a < queue.length; a++) {
      temp[(a + distance) % queue.length] = queue[a]
    }
  } else if (direction == "left") {
    for (var a = 0; a < queue.length; a++) {
      temp[a - distance >= 0 ? a - distance : a - distance + queue.length] =
        queue[a]
    }
  }
  temp.shift()
  return temp
}

////////////////////////////////////////////////////////

const fs = require("fs")
const [a, b] = fs.readFileSync("./dev/stdin").toString().trim().split("\n")

const [N, K] = a.split(" ").map((v) => +v)
const target = b.split(" ").map((v) => +v)

class Node {
  constructor(item) {
    this.item = item
    this.prev = null
    this.next = null
  }
}

class Deque {
  constructor() {
    this.head = null
    this.tail = null
    this.length = 0
  }

  push_front(item) {
    const node = new Node(item)
    if (this.size() == 0) {
      this.head = node
      this.tail = node
    } else {
      this.head.prev = node
      node.next = this.head
      this.head = node
    }
    this.length += 1
  }

  push_back(item) {
    const node = new Node(item)
    if (this.size() == 0) {
      this.head = node
      this.tail = node
    } else {
      this.tail.next = node
      node.prev = this.tail
      this.tail = node
    }
    this.length += 1
  }

  pop_front() {
    if (this.size() == 0) return -1
    const popItem = this.head
    this.head = this.head.next
    if (this.size() == 1) {
      this.head = null
    } else {
      this.head.prev = null
    }
    this.length -= 1
    return popItem.item
  }

  pop_back() {
    if (this.size() == 0) return -1
    const popItem = this.tail
    this.tail = this.tail.prev
    if (this.size() == 1) {
      this.tail = null
    } else {
      this.tail.next = null
    }
    this.length -= 1
    return popItem.item
  }

  size() {
    return this.length
  }

  empty() {
    if (this.length == 0) {
      return 1
    } else {
      return 0
    }
  }

  front() {
    if (this.empty() == 1) return -1
    return this.head.item
  }

  back() {
    if (this.empty() == 1) return -1
    return this.tail.item
  }
}

let answer = 0
let deque = new Deque()

for (let i = 1; i <= N; i++) {
  deque.push_back(i)
}

let position = []
for (let i = 0; i < K; i++) {
  position.push(target[i])
}

while (position.length > 0) {
  if (position[0] == 1) {
    position = position.map((v) => v - 1)
    deque.pop_front()
    position.shift()
  } else if (position[0] == deque.size()) {
    answer++
    deque.pop_front()
    position.shift()
  } else {
    if (deque.size() + 1 >= 2 * position[0]) {
      position = position.map((v) => {
        if (v == 1) {
          return (v = deque.size())
        }
        return v - 1
      })

      deque.push_back(deque.pop_front())
    } else {
      position = position.map((v) => {
        if (v == deque.size()) {
          return (v = 1)
        }
        return v + 1
      })
      deque.push_front(deque.pop_back())
    }
    answer++
  }
}
console.log(answer)
