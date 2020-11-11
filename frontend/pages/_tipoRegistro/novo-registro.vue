<template>
  <v-container>
  	<hearder-novo-registro :tipoRegistro="tipoRegistro" />
  <form-novo-registro/> 
	</v-container>
</template>

<script>

import Vuex from 'vuex'
import formNovoRegistro from '~/components/form-novo-registro.vue'
import hearderNovoRegistro from '~/components/header-novo-registro.vue' 

export default {
  
  components: {	
    formNovoRegistro, hearderNovoRegistro
  },

  asyncData (context) {
    const tipoRegistro = context.params.tipoRegistro
    return {tipoRegistro} 

  },
  data () {
    return {}
  }
}
</script>

<style>
</style>
