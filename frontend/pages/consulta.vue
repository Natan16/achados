<template>
 	<div><consulta-list :registros=registros :correspondencias=correspondencias > </consulta-list></div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import consultaList from '~/components/consulta-list.vue'


export default {

	components: {
    	consultaList,
  	},
  	
  	//tá tando unauthorized porque ele fala ajax login required no front
	asyncData(context) {
		//console.log(context.store.getters.logged_user)
		
		return AppApi.consulta_registros().then(result => {
	  		var registros = result.data
	  		console.log(registros)
			var correspondencias = [] 
			var registro
			for(registro in registros ){  	
		  		var corr = AppApi.lista_correspondencias(registro).then(result => {
		  			return result.data
		  		})
		  		correspondencias.push(corr)
	  		}
	  		console.log(correspondencias)
	  		return {
	    		registros, 
	  			correspondencias
	  		}
		})
	},


  	data () {
    	return {}
  	}
}
</script>

<style>
</style>
