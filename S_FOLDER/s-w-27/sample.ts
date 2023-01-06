function getRandom(n: number = 0): number {
  return Math.floor(Math.random() * n)
}

getRandom(99)

function queryById(idName: string): HTMLElement | null {
  return document.getElementById(idName)
}

let greetingMessage: string
greetingMessage = 1
greetingMessage = "gd"
greetingMessage = ["gd", "a"]
