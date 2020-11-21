<template>
 	<div><consulta-list :registros=registros > </consulta-list></div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import consultaList from '~/components/consulta-list.vue'


export default {

	components: {
    	consultaList,
  	},
  	
	asyncData(context) {
		
		/*Promisse.all([p1 , p2 , ... ]).then(results => {
			//faz alguma coisa
		})*/

		return AppApi.consulta_registros().then(result => {
	  		var registros = result.data
	  		for (var reg of registros){
	  			reg.correspondencias = []
	  		}
	  		return {
	    		registros
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
