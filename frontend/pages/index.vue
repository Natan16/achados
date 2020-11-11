<template>
<div>  
  <v-layout justify-center align-center>
    <v-btn color="error"  class="white--text" :to="{name: 'tipoRegistro-novo-registro', params:{tipoRegistro:'perdido'}}">Eu perdi um documento</v-btn>
    <v-btn color="success" :to="{name: 'tipoRegistro-novo-registro', params:{tipoRegistro: 'achado'}}">Eu achei um documento</v-btn>
  	
  </v-layout>
  <p></p>
  <div style="position: relative; width: 600px; height: 800px;">    

    <div style="position: absolute; bottom: 5px; ">
     <h2>Nossa missão</h2> 
    Dezenas de milhares de documentos são perdidos todo ano no Brasil. Muitas vezes, a pessoa que achou não se dá ao trabalho de levar o documento até o setor de achados e perdidos do orgão público resposável. E, ainda assim, a pessoa que perdeu tem que pagar alguma taxa. Essa plataforma tem como objetivo facilitar esse processo oferencendo, um serviço GRATUITO para conectar quem perdeu a quem achou um documento.  
    </div> 
   </div>

</div>

</template>

<script>
import Vuex from 'vuex'

export default {
  data () {
    return {}
  }
}
</script>

<style>
</style>
