<template>
<div>  
  <v-layout justify-center align-center>
    <v-btn color="rgba(255, 0, 0, 0.5)"  class="white--text" :to="{name: 'tipoRegistro-registro', params:{tipoRegistro:'perdido'}}">Eu perdi um documento</v-btn>
    <v-btn color="success" :to="{name: 'tipoRegistro-registro', params:{tipoRegistro:'achado'}}">Eu achei um documento</v-btn>
  	
  </v-layout>
  <p></p>
  <div style="position: relative; width: 600px; height: 800px;">    

    <div style="position: absolute; bottom: 5px; ">
     <h2>Nossa missão</h2> 
    Mais de X mil documentos são peridos por ano. Muitas vezes não são encontrados porque ... . Mesmo quando encontrado
  tem que ir nos Correios e pagar uma taxa de Y reais. Essa plataforma tem como missão facilitar esse processo blau
    </div>
   </div>

</div>

</template>

<script>

//aidiconar na parte de baixo qual é nossa missão ( o objetivo do site )
export default {
  data () {
    return {}
  }
}
</script>

<style>
</style>
