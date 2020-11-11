<template>
  	<v-container>
		<!-- <v-layout justify-left> -->
		<!--  <v-btn-toggle
	        v-model="toggle_registro"
	        rounded
	        mandatory
	         >
	        <v-btn>
	          Novo Registro
	        </v-btn>
	        <v-btn>
	          Consultar Registro
	        </v-btn>
        	</v-btn-toggle> -->
        <!-- </v-layout> -->
        <!-- não precisa que logged user esteja como parâmetro -->
		<form-novo-registro> 
		</form-novo-registro> 

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
