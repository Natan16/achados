<template>
  <v-layout justify-left>
    <form-achado/> <!-- pode passar como parêmtro para o form genérico que ele é achado -->
  </v-layout>
</template>

<script>

import formAchado from '~/components/form-achado.vue'
import Vuex from 'vuex'
//os formulários para achados e perdidos são iguais, o que muda é o parâmetro que depende da escolha no Menu
export default {
  components: {
    formAchado
  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
