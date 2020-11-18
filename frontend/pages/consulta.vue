<template>
 	<div><consulta-list :registros=registros :correspondencias=correspondencias ></consulta-list></div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import consultaList from '~/components/consulta-list.vue'


export default {

	components: {
    	consultaList,
  	},
  	
  	computed: Object.assign(
      {},
      Vuex.mapGetters([
        'logged_user'
      ])
    ),

	asyncData(context) { 
		return AppApi.consulta_registros(context.logged_user).then(result => {
	  		var registros = result.data
			var correspondencias = [] 
			var registro
			for(registro in registros ){  	
		  		correspondencias.push(AppApi.lista_correspondencias(registro).then(result => {
		  			return result.data
		  		}))
	  		}
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
