import { kitty, update } from "./prototest"

update
kitty

import axios from "axios"

export const test = function () {
  axios({
    method: "get",
    url: "https://dog.ceo/api/breeds/image/raasdfasdfasdfsndom",
  })
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err, "에러에러!!!!")
      return axios({
        method: "get",
        url: "https://dog.ceo/api/breeds/image/random",
      }).then((res) => {
        console.log("됨?", res)
      })
    })
}
