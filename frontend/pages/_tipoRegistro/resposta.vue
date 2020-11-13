<template>
  <!-- colocar isso aqui dentro de um componente à parte -->
  <div>

    <v-container v-if="!encontrado" >
      <h1 >
        Por enquanto nenhuma correspondência foi encontrada para o seu 
        registro de documento {{tipoRegistro}}.
      </h1>
      <br> 
      <h1>
        Um e-mail será enviado à você assim que 
        houver alguma novidade relativa à sua solicitação. 
      </h1>
      <br>
      <h1>
         Obrigado!
      </h1> <!-- fazer algum elogio maior à quem achou o documento -->
         
    </v-container>

    <v-container v-if="encontrado" >
      
      <h1 >
          As seguintes correspondências foram encontradas para o seu registro
      </h1>
      <br>
       <doc-list :correspondencias="correspondencias">
       </doc-list > 
    </v-container>
  </div>
</template>

<script>

import Vuex from 'vuex'
import AppApi from '~apijs'
import { mapGetters } from 'vuex'
import docList from '~/components/doc-list.vue'

export default {
  components: {
    docList , 
  },
    
  asyncData(context) {
    //console.log(context.store.getters['formulario/documento'])
    let documento = context.store.getters.documento
    let solicitante = context.store.getters.solicitante
    let tipoRegistro = context.params.tipoRegistro
    let tipoRegistroCorr = tipoRegistro === 'achado' ? 'perdido' : 'achado'
    //documento nao pode ser passado via store
    return AppApi.lista_correspondencias( documento , tipoRegistroCorr).then(result => {  
      return { correspondencias : result.data.correspondencias , 
              encontrado: result.data.correspondencias.length > 0 ,
              documento : documento , 
              solicitante : solicitante,
              tipoRegistro : tipoRegistro
            }
      })

    //faltou mandar email pra todas as correspondências avisando que solicitante achou. Pode fazer isso em mounted, de maneira assícrona
  },

  mounted() {
    //this.solicitante.nome , this.solicitante.email
    //AppApi.enviar_email( )
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
