<template>
  <v-layout justify-center align-center>
    <v-btn color="rgba(255, 0, 0, 0.5)" :to="{name: 'perdidos'}">Eu perdi um documento</v-btn>
    <v-btn color="success" :to="{name: 'achados'}">Eu achei um documento</v-btn>
  </v-layout>
</template>

<script>
//aidiconar na parte de baixo qual é nossa missão ( o objetivo do site )
export default {
  data () {
    return {}
  }
}
</script>

<style>
</style>
