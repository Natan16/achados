<template>
  <div>

    <nao-encontrado v-if="!encontrado" />
    <v-container v-if="encontrado" >
      <h1 style="color:#1565C0">
          As seguintes correspondências foram encontradas para o seu registro :
      </h1>
      <br>
       <doc-list :correspondencias="correspondencias" :tipoRegistro="tipoRegistro">
       </doc-list > 
    </v-container>
  </div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import { mapGetters } from 'vuex'
import docList from '~/components/doc-list.vue'
import naoEncontrado from '~/components/nao-encontrado.vue'

export default {
  components: {
    naoEncontrado,
    docList, 
  },
  
  asyncData(context) {
    //console.log(context.store.getters['formulario/documento'])
    let documento = context.store.getters.documento
    let solicitante = context.store.getters.solicitante
    let tipoRegistro = context.params.tipoRegistro
    let tipoRegistroCorr = tipoRegistro === 'achado' ? 'perdido' : 'achado'
    //documento nao pode ser passado via store
    return AppApi.lista_correspondencias( documento , tipoRegistroCorr).then(result => {  
      console.log(result)
      return { 
              correspondencias : result.data, 
              encontrado: result.data.length > 0 ,
              documento : documento , 
              solicitante : solicitante,
              tipoRegistro : tipoRegistro
            }
      })

    //faltou mandar email pra todas as correspondências avisando que solicitante achou. Pode fazer isso em mounted, de maneira assícrona
  },

  mounted() {
    //for corr in this.correspondencias.length, 
    //AppApi.envia_email( )
  },

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
