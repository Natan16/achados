<template>
 	<div></div>
</template>

<script>


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
