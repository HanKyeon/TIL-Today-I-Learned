<template>
  <div>
    <h1>개</h1>
    <input type="text" v-model="inputData" @keyup.enter="callDog" />
    <br />
    <p v-if="!imgSrc">{{ msg }}</p>
    <img v-if="imgSrc" :src="imgSrc" alt="개" />
  </div>
</template>

<script>
// https://dog.ceo/dog-api/
// Husky. 품종을 입력 데이터로 받을 것임.
import axios from "axios"

export default {
  name: "DogView",
  data() {
    return {
      inputData: "",
      imgSrc: null,
      msg: "로딩중",
    }
  },
  computed: {
    breedData() {
      return this.inputData
    },
  },
  methods: {
    callDog() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method: "get",
        url: dogImageUrl,
      })
        .then((response) => {
          console.log(response)
          this.imgSrc = response.data.message
        })
        .catch((error) => {
          this.msg = `${this.$route.params.breed}는 없는 품종 입니다.`
          this.$router.push("/404")
          console.error(error.response)
        })
    },
  },
  created() {
    this.callDog()
  },
}
</script>

<style></style>
