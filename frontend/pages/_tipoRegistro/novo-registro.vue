<template>
  	<v-container>
  		<!-- <hearder-novo-registro/>  criar um hearder pelo menos escrito: Registro de Documento Perdido-->
		<form-novo-registro/> 
	</v-container>
</template>

<script>

import Vuex from 'vuex'
import formNovoRegistro from '~/components/form-novo-registro.vue'

export default {
  
  components: {	
    formNovoRegistro,
  },

  asyncData (context) {
    const tipoRegistro = context.params.tipoRegistro
    return {tipoRegistro} 

  },
  data () {
    return {toggle_registro:0,}
  }
}
</script>

<style>
</style>
