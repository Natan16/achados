<template>
  <!-- colocar isso aqui dentro de um componente à parte -->
  <div>
    <v-container >
      <h1 style="color:#1565C0">
        Por enquanto nenhuma correspondência foi encontrada para o seu 
        registro de documento {{tipoRegistro}}.
      </h1>
      <br> 
      <h1 style="color:#1565C0">
        Um e-mail será enviado à você assim que 
        houver alguma novidade relativa à sua solicitação. 
      </h1>
      <br>
      <h1 style="color:#1565C0">
         Obrigado!
      </h1> <!-- fazer algum elogio maior à quem achou o documento -->
         
    </v-container>
  </div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'

export default {
  props:['encontrado'],
  data () {
    return {
    }
  }
}
//pegar o caso de o mesmo loggedUser já ter registrado esse documento, vai fazer algo a respeito? 
//Sim, apenas quando for implementado o usuário logado 
</script>

<style>
  h1 {text-align: center;color:blue;}
</style>
