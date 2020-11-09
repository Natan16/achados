<template>
  	<v-container>
		<!-- <v-layout justify-left> -->
		 <v-btn-toggle
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
        	</v-btn-toggle>
        <!-- </v-layout> -->
	    <form-novo-registro  v-if="toggle_registro == 0" >
		</form-novo-registro> <!-- pode passar como parêmtro para o form genérico que ele é achado -->
		<form-consulta-registro  v-if="toggle_registro == 1" tipoRegistro="tipoRegistro">
		</form-consulta-registro> <!-- pode passar como parêmtro para o form genérico que ele é achado -->
		
	</v-container>
</template>

<script>

import formNovoRegistro from '~/components/form-novo-registro.vue'
import formConsultaRegistro from '~/components/form-consulta-registro.vue'
import Vuex from 'vuex'
//os formulários para achados e perdidos são iguais, o que muda é o parâmetro que depende da escolha no Menu
export default {
  
  components: {
  	
    formNovoRegistro,
    formConsultaRegistro,
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
