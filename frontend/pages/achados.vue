<template>
  <v-layout justify-left>
    <form-achado/>
  </v-layout>
</template>

<script>

import formAchado from '~/components/form-achado.vue'
import Vuex from 'vuex'

export default {
  layout: 'complex',
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
